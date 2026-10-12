# Test Cases Specification & Verification Report
## IT Help Desk Ticket Management System

This document outlines the systematic test cases designed, executed, and verified for the **IT Help Desk Ticket Management System**. All automated tests have been executed using Python's standard `unittest` framework against an isolated SQLite test database.

---

### Test Environment Summary
- **Operating System:** macOS (Apple Silicon / Darwin)
- **Runtime:** Python 3.14 / Flask 3.1
- **Database Engine:** SQLite 3
- **Test Framework:** `unittest` with Flask Test Client
- **Total Automated Test Cases:** 18
- **Pass Rate:** 100% (18 Passed, 0 Failed, 0 Skipped)

---

### Test Cases Table

| Test Case ID | Feature / Module | Test Objective | Input / Action | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | Database Setup | Verify schema creation and default seeding on startup | Invoke `init_db()` and `seed_db()` | Tables `users`, `tickets`, and `ticket_notes` created; initial admin and 8 demo tickets populated | Verified via test suite & CLI (`flask init-db`) | **PASS** |
| **TC-02** | Dashboard | Verify dashboard metrics calculation | `GET /dashboard` | Returns HTTP 200; displays dynamic counts for Total, Open, In Progress, Resolved, and High Priority | HTTP 200; all 5 metrics accurately match SQLite record counts | **PASS** |
| **TC-03** | Dashboard | Verify root URL redirect / render | `GET /` | Root route renders the main dashboard seamlessly | HTTP 200; rendered `dashboard.html` | **PASS** |
| **TC-04** | Ticket Creation | Verify form loading | `GET /tickets/new` | Returns HTTP 200 with all form fields and CSRF token | HTTP 200; form rendered with proper inputs | **PASS** |
| **TC-05** | Ticket Creation | Verify submission with valid inputs | `POST /tickets/new` with title, valid email, category, priority, description | Ticket inserted into database with generated ID (e.g. `HD-1009`); redirects to ticket details page | HTTP 302 -> 200; record stored in SQLite; flash success message shown | **PASS** |
| **TC-06** | Ticket Validation | Reject short title (< 5 characters) | `POST /tickets/new` with `title: "Bug"` | Returns HTTP 400 Bad Request; flash validation error message | HTTP 400; message: "between 5 and 120 characters" | **PASS** |
| **TC-07** | Ticket Validation | Reject invalid email format | `POST /tickets/new` with `email: "not-an-email"` | Returns HTTP 400 Bad Request; record rejected | HTTP 400; message: "valid email address is required" | **PASS** |
| **TC-08** | Ticket Validation | Reject invalid category | `POST /tickets/new` with unregistered category | Returns HTTP 400 Bad Request; prevents arbitrary inputs | HTTP 400; message: "valid IT category" | **PASS** |
| **TC-09** | Ticket Queue | Verify ticket queue display | `GET /tickets` | Returns HTTP 200 with table containing all active tickets | HTTP 200; seeded tickets (HD-1001 to HD-1008) listed | **PASS** |
| **TC-10** | Ticket Search | Verify search by unique Ticket ID | `GET /tickets?q=HD-1002` | Filters view to display only ticket HD-1002 | HTTP 200; HD-1002 displayed; non-matching tickets filtered out | **PASS** |
| **TC-11** | Ticket Search | Verify search by title keyword | `GET /tickets?q=printer` | Returns tickets matching "printer" in title or description | HTTP 200; ticket HD-1005 (Network printer offline) displayed | **PASS** |
| **TC-12** | Ticket Filter | Verify filtering by status | `GET /tickets?status=Resolved` | Displays only resolved tickets | HTTP 200; only resolved tickets (HD-1005, HD-1006, HD-1008) shown | **PASS** |
| **TC-13** | Ticket Filter | Verify filtering by priority | `GET /tickets?priority=Low` | Displays only tickets with Low priority | HTTP 200; HD-1004 and HD-1008 displayed; High priority omitted | **PASS** |
| **TC-14** | Ticket Details | Inspect existing ticket record | `GET /tickets/HD-1001` | Returns HTTP 200 with ticket metadata, full description, and notes timeline | HTTP 200; all attributes and activity history rendered | **PASS** |
| **TC-15** | Error Handling | Handle nonexistent ticket ID | `GET /tickets/HD-9999` | Returns HTTP 404 Not Found using custom error template | HTTP 404; friendly error page displayed without stack trace leaks | **PASS** |
| **TC-16** | Authentication | Reject invalid login credentials | `POST /login` with wrong password | Returns HTTP 401 Unauthorized; displays error alert | HTTP 401; "Invalid credentials. Please verify..." displayed | **PASS** |
| **TC-17** | Authentication | Accept valid credentials & handle logout | `POST /login` with `admin` / `Admin@123`; then `GET /logout` | Login sets session cookies; redirect to dashboard; logout terminates session | HTTP 302 -> 200; user session established and cleanly cleared on logout | **PASS** |
| **TC-18** | Access Control | Prevent unauthenticated status updates | `POST /tickets/HD-1001/update` without session | Intercepted by `@login_required`; redirects to `/login` with `next` parameter | HTTP 302 redirect to `/login`; unauthorized update blocked | **PASS** |
| **TC-19** | Staff Management | Allow authenticated staff to update ticket | Authenticated `POST /tickets/HD-1001/update` with `status: In Progress`, `priority: Medium` | Ticket updated in DB; automated audit log entry appended to `ticket_notes` | HTTP 302 -> 200; status changed, updated timestamp refreshed, note logged | **PASS** |
| **TC-20** | Security | Enforce CSRF token verification | `POST /tickets/new` with `CSRF_ENABLED=True` and omitted token | Request rejected with HTTP 403 Forbidden | HTTP 403; forbidden error returned | **PASS** |

---

### Test Execution Command
To re-run the automated test suite locally:
```bash
./venv/bin/python -m unittest -v tests/test_app.py
```
