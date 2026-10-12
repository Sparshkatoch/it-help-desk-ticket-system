"""
Database management helper module for IT Help Desk Ticket Management System.
Handles SQLite connection pooling in Flask application context, schema initialization,
sample data seeding, and secure administrative user creation.
"""

import os
import sqlite3
from datetime import datetime, timedelta
from flask import g, current_app
from werkzeug.security import generate_password_hash

DEFAULT_DB_PATH = os.path.join(os.path.dirname(__file__), 'helpdesk.db')


def get_db():
    """
    Get a database connection for the current request context.
    Configures sqlite3.Row row factory for dict-like access and enables foreign keys.
    """
    if 'db' not in g:
        db_path = current_app.config.get('DATABASE', DEFAULT_DB_PATH)
        # Ensure parent directory exists
        os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
        g.db = sqlite3.connect(db_path)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db


def close_db(e=None):
    """Closes the database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db(app=None):
    """Initializes the database schema using schema.sql."""
    schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
    if app:
        with app.app_context():
            db = get_db()
            with open(schema_path, 'r', encoding='utf-8') as f:
                db.executescript(f.read())
            db.commit()
    else:
        db = get_db()
        with open(schema_path, 'r', encoding='utf-8') as f:
            db.executescript(f.read())
        db.commit()


def generate_ticket_id(db):
    """
    Generates a human-friendly unique ticket identifier (e.g. HD-1001).
    Finds the maximum existing numeric suffix and increments by 1.
    """
    cursor = db.cursor()
    cursor.execute("SELECT ticket_id FROM tickets ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    if not row:
        return "HD-1001"
    
    last_id = row['ticket_id']
    try:
        if last_id.startswith("HD-"):
            num = int(last_id.split("-")[1])
            return f"HD-{num + 1}"
    except (ValueError, IndexError):
        pass
    
    # Fallback using count
    cursor.execute("SELECT COUNT(*) as cnt FROM tickets")
    count = cursor.fetchone()['cnt']
    return f"HD-{1001 + count}"


def create_user(db, username, email, password, role='staff'):
    """
    Inserts a user with a securely hashed password.
    Returns True if created, or False if username/email already exists.
    """
    cursor = db.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
    if cursor.fetchone():
        return False
    
    password_hash = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)",
        (username, email, password_hash, role)
    )
    db.commit()
    return True


def seed_db(db):
    """
    Safely seeds initial demonstration data (admin user and realistic tickets)
    without creating duplicate data if rows already exist.
    """
    cursor = db.cursor()
    
    # 1. Seed default administrator if no users exist
    cursor.execute("SELECT COUNT(*) as cnt FROM users")
    if cursor.fetchone()['cnt'] == 0:
        create_user(db, 'admin', 'admin@helpdesk.local', 'Admin@123', role='admin')
        create_user(db, 'support_agent', 'agent@helpdesk.local', 'Agent@123', role='staff')

    # 2. Seed realistic tickets if no tickets exist
    cursor.execute("SELECT COUNT(*) as cnt FROM tickets")
    if cursor.fetchone()['cnt'] == 0:
        now = datetime.now()
        sample_tickets = [
            (
                "HD-1001",
                "Blue screen error on developer workstation",
                "Laptop randomly crashes with SYSTEM_SERVICE_EXCEPTION error after the latest OS patch.",
                "Aditi Sharma",
                "aditi.sharma@college.edu",
                "Computer or laptop issues",
                "High",
                "Open",
                "Computer Engineering",
                (now - timedelta(days=2, hours=4)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(days=2, hours=4)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1002",
                "Campus Wi-Fi authentication timeout in Block B",
                "Students and faculty unable to authenticate to the 802.1X enterprise network in 3rd floor lab.",
                "Prof. Rajesh Verma",
                "r.verma@college.edu",
                "Internet and network problems",
                "High",
                "In Progress",
                "Information Technology",
                (now - timedelta(days=1, hours=8)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1003",
                "Python IDE & GCC compiler package installation error",
                "Permission denied error when attempting to install virtualenv and C++ compiler packages in Lab 4.",
                "Rohan Gupta",
                "rohan.gupta@student.college.edu",
                "Software errors",
                "Medium",
                "In Progress",
                "Computer Engineering",
                (now - timedelta(days=1, hours=2)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1004",
                "Student ERP portal password reset request",
                "Unable to reset portal password. Self-service OTP is not arriving on the registered phone number.",
                "Priya Nair",
                "priya.nair@student.college.edu",
                "Login and account access",
                "Low",
                "Open",
                "Electronics & Telecom",
                (now - timedelta(hours=18)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(hours=18)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1005",
                "Network printer offline in Examination Section",
                "HP LaserJet Pro 400 paper jam cleared, but device shows network error and will not accept print jobs.",
                "Sunil Deshmukh",
                "s.deshmukh@admin.college.edu",
                "Printer and peripheral issues",
                "High",
                "Resolved",
                "Administration & Exam Cell",
                (now - timedelta(days=3)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1006",
                "Projector HDMI port flickering in Seminar Hall 2",
                "Display drops signal every few minutes during multimedia presentations.",
                "Dr. Meenakshi Sundaram",
                "m.sundaram@college.edu",
                "Other technical problems",
                "Medium",
                "Resolved",
                "Mechanical Engineering",
                (now - timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1007",
                "GitLab local server certificate expired warning",
                "Browser throws SSL certificate invalid warning when cloning projects from internal college server.",
                "Karan Mehta",
                "karan.m@student.college.edu",
                "Software errors",
                "High",
                "Open",
                "Information Technology",
                (now - timedelta(hours=6)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(hours=6)).strftime('%Y-%m-%d %H:%M:%S')
            ),
            (
                "HD-1008",
                "Library digital kiosk mouse not responding",
                "USB optical mouse on terminal #4 is unresponsive after reboot.",
                "Anita Kulkarni",
                "library@college.edu",
                "Printer and peripheral issues",
                "Low",
                "Resolved",
                "Central Library",
                (now - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S'),
                (now - timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S')
            )
        ]

        cursor.executemany(
            """
            INSERT INTO tickets (
                ticket_id, title, description, requester_name, requester_email,
                category, priority, status, department, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            sample_tickets
        )
        
        # Add sample notes for resolved / in-progress tickets
        sample_notes = [
            (2, "support_agent", "Inspected AP-302 in 3rd floor corridor. Found DHCP pool exhaustion on VLAN 20. Reconfiguring lease time.", (now - timedelta(hours=3)).strftime('%Y-%m-%d %H:%M:%S')),
            (3, "admin", "Granted temporary local administrator privileges to student workstation. Package setup verified.", (now - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M:%S')),
            (5, "support_agent", "Restarted print spooler service and updated static IP binding. Successfully printed 5 test pages.", (now - timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')),
            (6, "support_agent", "Replaced worn HDMI patch cable at the podium. Tested 4K video playback for 30 minutes with zero drops.", (now - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')),
            (8, "support_agent", "Replaced faulty USB cable; kiosk terminal tested and functioning normally.", (now - timedelta(days=4)).strftime('%Y-%m-%d %H:%M:%S'))
        ]
        cursor.executemany(
            "INSERT INTO ticket_notes (ticket_id, author, note, created_at) VALUES (?, ?, ?, ?)",
            sample_notes
        )
        db.commit()
