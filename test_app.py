"""
Automated Unit and Integration Test Suite
IT Help Desk Ticket Management System

Tests database initialization, ticket creation, validation rules,
search and filtering, authentication, authorization, and error handling.
"""

import os
import re
import tempfile
import unittest

from app import app
from database.db import get_db, init_db, seed_db, create_user


class HelpDeskTestCase(unittest.TestCase):
    def setUp(self):
        """Set up an isolated test database and test client before each test."""
        self.db_fd, self.db_path = tempfile.mkstemp(suffix='.db')
        app.config['DATABASE'] = self.db_path
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False  # Disabled during standard functional tests
        app.config['SECRET_KEY'] = 'test-secret-key-12345'
        
        self.client = app.test_client()

        with app.app_context():
            init_db()
            db = get_db()
            seed_db(db)

    def tearDown(self):
        """Clean up the temporary database file after each test."""
        os.close(self.db_fd)
        if os.path.exists(self.db_path):
            os.unlink(self.db_path)

    # -----------------------------------------------------------------------
    # 1. Dashboard & General Routes
    # -----------------------------------------------------------------------
    def test_dashboard_route_loads(self):
        """Test that the dashboard returns 200 OK and displays core metrics."""
        response = self.client.get('/dashboard')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('IT Operations Dashboard', content)
        self.assertIn('Total Tickets', content)
        self.assertIn('Open Tickets', content)
        self.assertIn('Resolved Tickets', content)

    def test_root_route_redirects_or_renders_dashboard(self):
        """Test that the root route / successfully serves the dashboard."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('IT Operations Dashboard', response.data.decode('utf-8'))

    # -----------------------------------------------------------------------
    # 2. Ticket Creation & Validation
    # -----------------------------------------------------------------------
    def test_create_ticket_page_loads(self):
        """Test that the ticket creation form page loads successfully."""
        response = self.client.get('/tickets/new')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Submit New IT Support Ticket', response.data.decode('utf-8'))

    def test_create_ticket_success(self):
        """Test creating a valid ticket persists to the DB and redirects to details."""
        payload = {
            'title': 'Network switch failure in Server Room',
            'description': 'Main rack switch is rebooting intermittently causing connection drops.',
            'requester_name': 'Sarah Connor',
            'requester_email': 'sarah.c@college.edu',
            'category': 'Internet and network problems',
            'priority': 'High',
            'department': 'Systems Engineering'
        }
        response = self.client.post('/tickets/new', data=payload, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('created successfully', content)
        self.assertIn('Network switch failure in Server Room', content)

        # Verify record exists in SQLite
        with app.app_context():
            db = get_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM tickets WHERE title = ?", (payload['title'],))
            ticket = cursor.fetchone()
            self.assertIsNotNone(ticket)
            self.assertEqual(ticket['requester_name'], 'Sarah Connor')
            self.assertEqual(ticket['status'], 'Open')
            self.assertEqual(ticket['priority'], 'High')
            self.assertTrue(ticket['ticket_id'].startswith('HD-'))

    def test_create_ticket_validation_errors(self):
        """Test that submitting invalid or missing data returns 400 Bad Request."""
        # Test 1: Title too short
        bad_payload = {
            'title': 'Bug',
            'description': 'Something is broken here.',
            'requester_name': 'Test User',
            'requester_email': 'test@example.com',
            'category': 'Software errors',
            'priority': 'Low'
        }
        res = self.client.post('/tickets/new', data=bad_payload)
        self.assertEqual(res.status_code, 400)
        self.assertIn('between 5 and 120 characters', res.data.decode('utf-8'))

        # Test 2: Invalid Email
        bad_payload['title'] = 'Valid Title Length'
        bad_payload['requester_email'] = 'not-an-email'
        res = self.client.post('/tickets/new', data=bad_payload)
        self.assertEqual(res.status_code, 400)
        self.assertIn('valid email address is required', res.data.decode('utf-8'))

        # Test 3: Invalid Category
        bad_payload['requester_email'] = 'valid@example.com'
        bad_payload['category'] = 'Nonexistent Category'
        res = self.client.post('/tickets/new', data=bad_payload)
        self.assertEqual(res.status_code, 400)
        self.assertIn('valid IT category', res.data.decode('utf-8'))

    # -----------------------------------------------------------------------
    # 3. Ticket Listing, Search & Filtering
    # -----------------------------------------------------------------------
    def test_tickets_listing_loads(self):
        """Test that the tickets list renders seeded tickets."""
        response = self.client.get('/tickets')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('IT Support Tickets', content)
        self.assertIn('HD-1001', content)

    def test_ticket_search_by_id(self):
        """Test searching tickets by exact ticket ID."""
        response = self.client.get('/tickets?q=HD-1002')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('HD-1002', content)
        self.assertNotIn('HD-1001', content)

    def test_ticket_search_by_title_keyword(self):
        """Test searching tickets by keyword in title."""
        response = self.client.get('/tickets?q=printer')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('HD-1005', content)

    def test_ticket_filter_by_status(self):
        """Test filtering tickets by status."""
        response = self.client.get('/tickets?status=Resolved')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('HD-1005', content)
        self.assertNotIn('HD-1001', content)  # HD-1001 is Open

    def test_ticket_filter_by_priority(self):
        """Test filtering tickets by priority."""
        response = self.client.get('/tickets?priority=Low')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('HD-1004', content)
        self.assertNotIn('HD-1001', content)  # HD-1001 is High

    # -----------------------------------------------------------------------
    # 4. Ticket Details & 404 Handling
    # -----------------------------------------------------------------------
    def test_ticket_details_existing(self):
        """Test viewing an existing ticket details page."""
        response = self.client.get('/tickets/HD-1001')
        self.assertEqual(response.status_code, 200)
        content = response.data.decode('utf-8')
        self.assertIn('HD-1001', content)
        self.assertIn('Blue screen error on developer workstation', content)
        self.assertIn('Aditi Sharma', content)

    def test_ticket_details_nonexistent(self):
        """Test requesting a nonexistent ticket ID returns 404."""
        response = self.client.get('/tickets/HD-9999')
        self.assertEqual(response.status_code, 404)
        self.assertIn('404', response.data.decode('utf-8'))

    # -----------------------------------------------------------------------
    # 5. Authentication & Staff Authorization
    # -----------------------------------------------------------------------
    def test_login_page_loads(self):
        """Test that the login page loads."""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Staff Portal Login', response.data.decode('utf-8'))

    def test_login_invalid_credentials(self):
        """Test login fails with incorrect password."""
        response = self.client.post('/login', data={
            'username': 'admin',
            'password': 'WrongPassword123'
        })
        self.assertEqual(response.status_code, 401)
        self.assertIn('Invalid credentials', response.data.decode('utf-8'))

    def test_login_success_and_logout(self):
        """Test successful login and subsequent logout."""
        # 1. Login with seeded credentials
        login_resp = self.client.post('/login', data={
            'username': 'admin',
            'password': 'Admin@123'
        }, follow_redirects=True)
        self.assertEqual(login_resp.status_code, 200)
        self.assertIn('Logged in as Admin', login_resp.data.decode('utf-8'))

        # 2. Logout
        logout_resp = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(logout_resp.status_code, 200)
        self.assertIn('safely logged out', logout_resp.data.decode('utf-8'))

    def test_unauthorized_ticket_update_redirects_to_login(self):
        """Test unauthenticated user cannot update ticket status."""
        response = self.client.post('/tickets/HD-1001/update', data={
            'status': 'Resolved',
            'priority': 'Low'
        })
        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login', response.headers['Location'])

    def test_authorized_ticket_status_update(self):
        """Test authenticated staff can successfully update ticket status and priority."""
        with self.client:
            # Login first
            self.client.post('/login', data={
                'username': 'support_agent',
                'password': 'Agent@123'
            })

            # Update ticket HD-1001
            update_resp = self.client.post('/tickets/HD-1001/update', data={
                'status': 'In Progress',
                'priority': 'Medium',
                'note': 'Investigating crash dump files.'
            }, follow_redirects=True)

            self.assertEqual(update_resp.status_code, 200)
            self.assertIn('updated successfully', update_resp.data.decode('utf-8'))

            # Verify in DB
            with app.app_context():
                db = get_db()
                cursor = db.cursor()
                cursor.execute("SELECT status, priority FROM tickets WHERE ticket_id = 'HD-1001'")
                t = cursor.fetchone()
                self.assertEqual(t['status'], 'In Progress')
                self.assertEqual(t['priority'], 'Medium')

                # Verify note was created
                cursor.execute("SELECT note FROM ticket_notes WHERE ticket_id = (SELECT id FROM tickets WHERE ticket_id = 'HD-1001')")
                notes = [row['note'] for row in cursor.fetchall()]
                self.assertTrue(any('Investigating crash dump files' in n for n in notes))

    # -----------------------------------------------------------------------
    # 6. CSRF Protection Enforced
    # -----------------------------------------------------------------------
    def test_csrf_protection_blocks_post_when_enabled(self):
        """Test that state-changing POST requests without CSRF token are blocked with 403."""
        app.config['CSRF_ENABLED'] = True
        try:
            response = self.client.post('/tickets/new', data={
                'title': 'Test CSRF Protection',
                'description': 'Testing whether CSRF validation blocks unauthorized POST.',
                'requester_name': 'Test',
                'requester_email': 'test@example.com',
                'category': 'Software errors',
                'priority': 'Low'
            })
            self.assertEqual(response.status_code, 403)
        finally:
            app.config['CSRF_ENABLED'] = False


if __name__ == '__main__':
    unittest.main()
