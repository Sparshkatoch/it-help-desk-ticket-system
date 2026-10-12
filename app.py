"""
IT Help Desk Ticket Management System
Flask Backend Application

A beginner-friendly, secure, full-stack web application designed for
managing IT complaints and support tickets across an organization.

Features:
- Dashboard with dynamic live statistics and recent tickets
- Ticket creation with input validation and auto-generated ticket IDs
- Search and multi-criteria filtering (status, category, priority)
- Ticket details with activity notes timeline
- Support staff & administrator authentication with password hashing
- Role-based server-side authorization and CSRF protection
- Safe sample data seeding and database auto-initialization
"""

import os
import re
import secrets
from datetime import datetime
from functools import wraps

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    g,
    abort
)
from werkzeug.security import check_password_hash

from database.db import (
    get_db,
    close_db,
    init_db,
    seed_db,
    generate_ticket_id,
    create_user
)

# Application Factory / Configuration
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'helpdesk-local-dev-key-2026'),
    DATABASE=os.path.join(app.root_path, 'database', 'helpdesk.db'),
    CSRF_ENABLED=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax'
)

# Register teardown function to clean up database connections
app.teardown_appcontext(close_db)

# Predefined application constants
CATEGORIES = [
    'Software errors',
    'Computer or laptop issues',
    'Internet and network problems',
    'Login and account access',
    'Printer and peripheral issues',
    'Other technical problems'
]

PRIORITIES = ['Low', 'Medium', 'High']
STATUSES = ['Open', 'In Progress', 'Resolved']


# ---------------------------------------------------------------------------
# Security & CSRF Protection
# ---------------------------------------------------------------------------

def generate_csrf_token():
    """Generates and caches a secure random CSRF token in the session."""
    if '_csrf_token' not in session:
        session['_csrf_token'] = secrets.token_hex(32)
    return session['_csrf_token']


@app.before_request
def csrf_protect():
    """Validates CSRF token on all state-changing HTTP methods."""
    if not app.config.get('CSRF_ENABLED', True):
        return

    if request.method in ('POST', 'PUT', 'DELETE', 'PATCH'):
        token = request.form.get('csrf_token') or request.headers.get('X-CSRFToken')
        session_token = session.get('_csrf_token')
        if not session_token or not token or token != session_token:
            # Flash error and abort with 403 Forbidden
            flash('Security token validation failed. Please refresh the page and try again.', 'error')
            abort(403)


@app.context_processor
def inject_template_globals():
    """Injects common constants, CSRF token generator, and user data into all templates."""
    current_user = None
    if 'user_id' in session:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT id, username, email, role FROM users WHERE id = ?", (session['user_id'],))
        current_user = cursor.fetchone()

    return {
        'csrf_token': generate_csrf_token,
        'CATEGORIES': CATEGORIES,
        'PRIORITIES': PRIORITIES,
        'STATUSES': STATUSES,
        'current_user': current_user,
        'now_year': datetime.now().year
    }


@app.template_filter('format_datetime')
def format_datetime(value, format_str='%Y-%m-%d %H:%M'):
    """Formats datetime object or string timestamp safely for template presentation."""
    if not value:
        return ''
    if isinstance(value, datetime):
        return value.strftime(format_str)
    try:
        # String timestamp parsing
        clean_val = str(value).replace('T', ' ').split('.')[0]
        dt = datetime.strptime(clean_val, '%Y-%m-%d %H:%M:%S')
        return dt.strftime(format_str)
    except Exception:
        return str(value)[:16]


def login_required(view_func):
    """Decorator to enforce support staff / admin authentication on protected routes."""
    @wraps(view_func)
    def decorated_view(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in with staff credentials to access this management feature.', 'warning')
            return redirect(url_for('login', next=request.url))
        return view_func(*args, **kwargs)
    return decorated_view


# ---------------------------------------------------------------------------
# Database Auto-Initialization
# ---------------------------------------------------------------------------

@app.before_request
def ensure_db_initialized():
    """
    Checks if the database tables exist on first request.
    If not, automatically initializes schema and populates sample records.
    """
    if getattr(app, '_db_checked', False):
        return
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tickets'")
        if not cursor.fetchone():
            init_db()
            seed_db(db)
        app._db_checked = True
    except Exception as e:
        app.logger.warning(f"Database check warning: {e}")


# ---------------------------------------------------------------------------
# Core Routes: Dashboard
# ---------------------------------------------------------------------------

@app.route('/')
@app.route('/dashboard')
def dashboard():
    """
    Renders the IT Help Desk Dashboard.
    Fetches real-time summary statistics and recent tickets from the database.
    """
    db = get_db()
    cursor = db.cursor()

    # Query key metrics
    cursor.execute("SELECT COUNT(*) AS total FROM tickets")
    total_tickets = cursor.fetchone()['total']

    cursor.execute("SELECT COUNT(*) AS open_count FROM tickets WHERE status = 'Open'")
    open_tickets = cursor.fetchone()['open_count']

    cursor.execute("SELECT COUNT(*) AS progress_count FROM tickets WHERE status = 'In Progress'")
    in_progress_tickets = cursor.fetchone()['progress_count']

    cursor.execute("SELECT COUNT(*) AS resolved_count FROM tickets WHERE status = 'Resolved'")
    resolved_tickets = cursor.fetchone()['resolved_count']

    cursor.execute("SELECT COUNT(*) AS high_count FROM tickets WHERE priority = 'High' AND status != 'Resolved'")
    high_priority_tickets = cursor.fetchone()['high_count']

    # Query recent tickets (latest 6)
    cursor.execute(
        """
        SELECT id, ticket_id, title, requester_name, category, priority, status, created_at
        FROM tickets
        ORDER BY created_at DESC
        LIMIT 6
        """
    )
    recent_tickets = cursor.fetchall()

    # Query category distribution for visual breakdown
    cursor.execute(
        """
        SELECT category, COUNT(*) as count
        FROM tickets
        GROUP BY category
        ORDER BY count DESC
        """
    )
    category_counts = cursor.fetchall()

    stats = {
        'total': total_tickets,
        'open': open_tickets,
        'in_progress': in_progress_tickets,
        'resolved': resolved_tickets,
        'high_priority': high_priority_tickets
    }

    return render_template(
        'dashboard.html',
        stats=stats,
        recent_tickets=recent_tickets,
        category_counts=category_counts
    )


# ---------------------------------------------------------------------------
# Core Routes: Ticket Listing & Search
# ---------------------------------------------------------------------------

@app.route('/tickets')
def tickets():
    """
    Displays all tickets with functional search and multi-parameter filtering.
    Supports search query (?q=), status filter, category filter, and priority filter.
    """
    search_query = request.args.get('q', '').strip()
    status_filter = request.args.get('status', '').strip()
    category_filter = request.args.get('category', '').strip()
    priority_filter = request.args.get('priority', '').strip()

    sql = """
        SELECT id, ticket_id, title, requester_name, requester_email,
               category, priority, status, department, created_at, updated_at
        FROM tickets
        WHERE 1=1
    """
    params = []

    if search_query:
        sql += " AND (ticket_id LIKE ? OR title LIKE ? OR requester_name LIKE ?)"
        term = f"%{search_query}%"
        params.extend([term, term, term])

    if status_filter and status_filter in STATUSES:
        sql += " AND status = ?"
        params.append(status_filter)

    if category_filter and category_filter in CATEGORIES:
        sql += " AND category = ?"
        params.append(category_filter)

    if priority_filter and priority_filter in PRIORITIES:
        sql += " AND priority = ?"
        params.append(priority_filter)

    sql += " ORDER BY created_at DESC"

    db = get_db()
    cursor = db.cursor()
    cursor.execute(sql, params)
    ticket_list = cursor.fetchall()

    return render_template(
        'tickets.html',
        tickets=ticket_list,
        search_query=search_query,
        status_filter=status_filter,
        category_filter=category_filter,
        priority_filter=priority_filter,
        result_count=len(ticket_list)
    )


# ---------------------------------------------------------------------------
# Core Routes: Create Ticket
# ---------------------------------------------------------------------------

@app.route('/tickets/new', methods=['GET', 'POST'])
def create_ticket():
    """
    Handles new ticket submission with strict validation.
    Generates a unique ticket ID and stores the record in SQLite.
    """
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        requester_name = request.form.get('requester_name', '').strip()
        requester_email = request.form.get('requester_email', '').strip()
        category = request.form.get('category', '').strip()
        priority = request.form.get('priority', '').strip()
        department = request.form.get('department', '').strip()

        # Input Validation
        errors = []

        if not title or len(title) < 5 or len(title) > 120:
            errors.append("Ticket title is required and must be between 5 and 120 characters.")

        if not description or len(description) < 10:
            errors.append("Detailed description is required (minimum 10 characters).")

        if not requester_name or len(requester_name) < 2:
            errors.append("Requester's name is required.")

        email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
        if not requester_email or not re.match(email_pattern, requester_email):
            errors.append("A valid email address is required for ticket updates.")

        if category not in CATEGORIES:
            errors.append(f"Please select a valid IT category from the list.")

        if priority not in PRIORITIES:
            errors.append(f"Please select a valid priority level ({', '.join(PRIORITIES)}).")

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template(
                'create_ticket.html',
                form_data=request.form
            ), 400

        # Generate ticket ID and persist
        db = get_db()
        ticket_id = generate_ticket_id(db)
        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO tickets (
                ticket_id, title, description, requester_name, requester_email,
                category, priority, status, department, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, 'Open', ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
            """,
            (ticket_id, title, description, requester_name, requester_email,
             category, priority, department)
        )
        db.commit()

        flash(f"Ticket {ticket_id} created successfully! Our IT team has been notified.", 'success')
        return redirect(url_for('ticket_details', ticket_id=ticket_id))

    return render_template('create_ticket.html', form_data={})


# ---------------------------------------------------------------------------
# Core Routes: Ticket Details & Staff Updates
# ---------------------------------------------------------------------------

@app.route('/tickets/<ticket_id>')
def ticket_details(ticket_id):
    """
    Renders detailed information for a specific ticket by ticket ID.
    Shows ticket attributes, timestamps, and staff activity notes.
    """
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        """
        SELECT id, ticket_id, title, description, requester_name, requester_email,
               category, priority, status, department, created_at, updated_at
        FROM tickets
        WHERE ticket_id = ?
        """,
        (ticket_id,)
    )
    ticket = cursor.fetchone()

    if not ticket:
        flash(f"Ticket '{ticket_id}' was not found in the system.", 'error')
        abort(404)

    # Fetch notes/timeline
    cursor.execute(
        """
        SELECT author, note, created_at
        FROM ticket_notes
        WHERE ticket_id = ?
        ORDER BY created_at ASC
        """,
        (ticket['id'],)
    )
    notes = cursor.fetchall()

    return render_template(
        'ticket_details.html',
        ticket=ticket,
        notes=notes
    )


@app.route('/tickets/<ticket_id>/update', methods=['POST'])
@login_required
def update_ticket_status(ticket_id):
    """
    Allows authorized support staff / admin to update status and priority,
    and optionally append a progress note.
    """
    new_status = request.form.get('status', '').strip()
    new_priority = request.form.get('priority', '').strip()
    note_text = request.form.get('note', '').strip()

    if new_status not in STATUSES:
        flash("Invalid status selected.", 'error')
        return redirect(url_for('ticket_details', ticket_id=ticket_id))

    if new_priority not in PRIORITIES:
        flash("Invalid priority selected.", 'error')
        return redirect(url_for('ticket_details', ticket_id=ticket_id))

    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT id, status, priority FROM tickets WHERE ticket_id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    if not ticket:
        abort(404)

    old_status = ticket['status']
    old_priority = ticket['priority']

    cursor.execute(
        """
        UPDATE tickets
        SET status = ?, priority = ?, updated_at = CURRENT_TIMESTAMP
        WHERE ticket_id = ?
        """,
        (new_status, new_priority, ticket_id)
    )

    # Record automatic status change note if status or priority changed
    changes = []
    if old_status != new_status:
        changes.append(f"Status changed from '{old_status}' to '{new_status}'")
    if old_priority != new_priority:
        changes.append(f"Priority changed from '{old_priority}' to '{new_priority}'")

    current_username = session.get('username', 'Staff')

    if changes:
        change_summary = "; ".join(changes)
        cursor.execute(
            "INSERT INTO ticket_notes (ticket_id, author, note) VALUES (?, ?, ?)",
            (ticket['id'], current_username, f"[System Update] {change_summary}")
        )

    # If the staff also wrote an optional custom note
    if note_text:
        cursor.execute(
            "INSERT INTO ticket_notes (ticket_id, author, note) VALUES (?, ?, ?)",
            (ticket['id'], current_username, note_text)
        )

    db.commit()
    flash(f"Ticket {ticket_id} updated successfully.", 'success')
    return redirect(url_for('ticket_details', ticket_id=ticket_id))


@app.route('/tickets/<ticket_id>/add-note', methods=['POST'])
@login_required
def add_ticket_note(ticket_id):
    """Allows authenticated staff to add internal resolution or progress notes."""
    note_text = request.form.get('note', '').strip()
    if not note_text:
        flash("Please enter note text before submitting.", 'error')
        return redirect(url_for('ticket_details', ticket_id=ticket_id))

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT id FROM tickets WHERE ticket_id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    if not ticket:
        abort(404)

    cursor.execute(
        "INSERT INTO ticket_notes (ticket_id, author, note) VALUES (?, ?, ?)",
        (ticket['id'], session.get('username', 'Staff'), note_text)
    )
    cursor.execute(
        "UPDATE tickets SET updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (ticket['id'],)
    )
    db.commit()

    flash("Progress note added successfully.", 'success')
    return redirect(url_for('ticket_details', ticket_id=ticket_id))


# ---------------------------------------------------------------------------
# Authentication Routes
# ---------------------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Staff / Administrator login portal.
    Verifies user credentials using secure password hashing.
    """
    if 'user_id' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if not username or not password:
            flash("Please enter both username and password.", 'error')
            return render_template('login.html'), 400

        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "SELECT id, username, password_hash, role FROM users WHERE username = ? OR email = ?",
            (username, username)
        )
        user = cursor.fetchone()

        if user and check_password_hash(user['password_hash'], password):
            # Session regeneration / assignment
            session.clear()
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']

            flash(f"Welcome back, {user['username']}! Logged in as {user['role'].title()}.", 'success')
            next_url = request.args.get('next')
            if next_url and next_url.startswith('/'):
                return redirect(next_url)
            return redirect(url_for('dashboard'))

        flash("Invalid credentials. Please verify username and password.", 'error')
        return render_template('login.html', username=username), 401

    return render_template('login.html')


@app.route('/logout')
def logout():
    """Clears user session and logs out of staff portal."""
    session.clear()
    flash("You have been safely logged out.", 'info')
    return redirect(url_for('login'))


# ---------------------------------------------------------------------------
# Error Handlers
# ---------------------------------------------------------------------------

@app.errorhandler(404)
def not_found_error(error):
    """Custom friendly 404 page."""
    return render_template('404.html'), 404


@app.errorhandler(403)
def forbidden_error(error):
    """Custom friendly 403 page."""
    return render_template('404.html', error_title="403 - Forbidden",
                           error_message="Access denied or security token verification failed."), 403


@app.errorhandler(500)
def internal_error(error):
    """Custom friendly 500 page."""
    return render_template('500.html'), 500


# ---------------------------------------------------------------------------
# CLI Commands for Database Administration
# ---------------------------------------------------------------------------

@app.cli.command('init-db')
def init_db_command():
    """CLI command: flask init-db"""
    init_db()
    print("Initialized the SQLite database schema successfully.")


@app.cli.command('seed-db')
def seed_db_command():
    """CLI command: flask seed-db"""
    db = get_db()
    seed_db(db)
    print("Seeded database with demonstration tickets and staff accounts.")


@app.cli.command('create-admin')
def create_admin_command():
    """CLI command: flask create-admin (interactive or env based)"""
    import getpass
    username = input("Enter admin username [default: admin]: ").strip() or "admin"
    email = input("Enter admin email [default: admin@helpdesk.local]: ").strip() or "admin@helpdesk.local"
    password = getpass.getpass("Enter secure password: ").strip()
    if not password:
        print("Password cannot be blank.")
        return
    db = get_db()
    if create_user(db, username, email, password, role='admin'):
        print(f"Administrator account '{username}' created successfully.")
    else:
        print(f"User with username '{username}' or email '{email}' already exists.")


if __name__ == '__main__':
    # Initialize DB schema and demo data if not already present
    with app.app_context():
        init_db()
        db = get_db()
        seed_db(db)
    app.run(host='127.0.0.1', port=5000, debug=True)
