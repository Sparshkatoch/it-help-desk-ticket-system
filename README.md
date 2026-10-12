# IT Help Desk Ticket Management System

An intuitive, secure, and full-stack web application built for academic and institutional technical support management. Designed and developed as a 3rd-Year Engineering College Internship Project under the **Web and Software Applications** track.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1-black.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite3-lightgrey.svg)
![Tests](https://img.shields.io/badge/Tests-18%2F18%20Passed-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 1. Project Overview & Problem Statement

### Problem Statement
In educational campuses, colleges, and enterprise departments, technical complaints—ranging from laboratory workstation blue-screen errors to campus Wi-Fi outages and printer paper jams—are often reported through unorganized channels (such as casual verbal complaints or loose email inboxes). This leads to:
- Lost or forgotten requests with zero traceability.
- Inability to triage emergency outages over minor queries.
- Lack of accountability and timestamped technician logs.
- Zero administrative metrics on equipment reliability.

### The Solution
The **IT Help Desk Ticket Management System** provides a centralized, web-based portal connecting students, faculty, and administrative staff directly with IT support personnel. It enables self-service incident reporting with automatic unique ID generation, real-time operational dashboard analytics, multi-criteria filtering, and role-based technician lifecycle management.

---

## 2. Project Objectives
- **Centralize Complaint Ingestion:** Standardize IT support requests across 6 distinct technical categories.
- **Automated Tracking:** Generate human-readable sequential ticket IDs (e.g. `HD-1001`) upon submission.
- **Operational Intelligence:** Compute live dashboard statistics directly from the database (Total, Open, In Progress, Resolved, High Priority).
- **Search & Filter:** Allow instant query search and filtering by status, category, and priority.
- **Audited Lifecycle:** Enable authenticated support staff to transition ticket states and record diagnostic notes.
- **Beginner-Friendly & Zero-Cost:** Operate locally on macOS / VS Code with zero paid APIs or cloud dependencies.

---

## 3. Technology Stack

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Frontend** | HTML5, CSS3 (Custom), JavaScript (ES6) | Responsive modern UI with CSS Grid/Flexbox and CSS Variables; no heavy external UI library bloat. |
| **Backend** | Python 3, Flask 3.1+ | Lightweight, robust WSGI framework with clean routing, session handling, and Jinja2 templating. |
| **Database** | SQLite 3 | Serverless, zero-configuration transactional database engine stored in a single local file. |
| **Security** | Werkzeug & Secrets | PBKDF2-HMAC-SHA256 password hashing and session CSRF token protection. |
| **Testing** | Python `unittest` | Automated test suite verifying routes, database queries, access control, and edge cases. |

---

## 4. Key Features

- **Live Operations Dashboard:** Dynamic count cards for Total, Open, In Progress, Resolved, and High-Priority tickets, accompanied by category distribution bars and a recent tickets table.
- **Incident Reporting:** Form validation (title length, email format, whitelisted categories/priorities) with instant flash messages.
- **Search & Multi-Filter Queue:** Fast search across Ticket ID, Title, and Requester name, with multi-dropdown filtering.
- **Dedicated Ticket Details:** Chronological activity timeline log, full problem description, and print summary action.
- **Staff Authentication & Access Control:** Role-based security enforcing `@login_required` on state-changing management routes.
- **Defensive Engineering:** Parameterized queries preventing SQL Injection, session CSRF tokens, and custom 404/500 error boundaries.

---

## 5. Project Directory Structure

```text
it-helpdesk-ticket-system/
├── app.py                      # Core Flask application, routing, auth & error handlers
├── requirements.txt            # Python dependencies (Flask, python-dotenv, docx, pptx)
├── README.md                   # Complete GitHub project documentation
├── .gitignore                  # Git exclusion rules (venv, *.db, .DS_Store, secrets)
├── .env.example                # Sample environment configuration template
├── database/
│   ├── schema.sql              # Database DDL schema (users, tickets, ticket_notes)
│   ├── db.py                   # SQLite connection helpers, ID generator & safe seeder
│   └── helpdesk.db             # Local SQLite database file (excluded from git)
├── templates/
│   ├── base.html               # Master layout with responsive navbar, flash toasts, footer
│   ├── dashboard.html          # Live metrics cards, category progress bars, recent tickets
│   ├── tickets.html            # Searchable and filterable ticket queue table
│   ├── create_ticket.html      # Incident submission form with priority selector cards
│   ├── ticket_details.html     # Ticket metadata, description, timeline log & staff controls
│   ├── login.html              # Staff authentication portal with demo credentials notice
│   ├── 404.html                # Friendly custom 404 Not Found error template
│   └── 500.html                # Custom 500 Internal Server Error template
├── static/
│   ├── css/
│   │   └── style.css           # Master stylesheet (CSS variables, responsive grid, badges)
│   └── js/
│       └── script.js           # Mobile nav toggle, toast auto-dismiss, status confirmation
├── tests/
│   └── test_app.py             # 18 automated unit and integration tests (100% pass rate)
└── docs/
    ├── project_report.md       # Full 28-section academic internship project report
    ├── project_report.docx     # Editable Word report generated for college submission
    ├── presentation_outline.md # 10-slide evaluation presentation script
    ├── presentation.pptx       # Editable PowerPoint presentation for evaluation panel
    ├── viva_questions.md       # 30 targeted viva voce Q&As + 1-min & 2-min pitch scripts
    ├── test_cases.md           # Test cases specification and verification table
    └── generate_office_docs.py # Script to regenerate .docx and .pptx files
```

---

## 6. Local Setup & Execution Instructions (macOS & VS Code)

Follow these step-by-step instructions to set up and run the application on macOS using VS Code:

### Step 1: Open the Project in VS Code
1. Launch **Visual Studio Code**.
2. Select **File > Open Folder...** from the top menu bar.
3. Browse to and select the `it-helpdesk-ticket-system` folder.
4. Open the integrated terminal in VS Code: Press <kbd>Ctrl</kbd> + <kbd>`</kbd> (backtick) or select **Terminal > New Terminal**.

### Step 2: Verify Python Installation
Verify that Python 3 is installed on your MacBook:
```bash
python3 --version
```
*(Ensure Python 3.10 or newer is displayed).*

### Step 3: Create & Activate Virtual Environment
Create an isolated virtual environment:
```bash
python3 -m venv venv
```
Activate the virtual environment:
```bash
source venv/bin/activate
```
*(Your terminal prompt will now show `(venv)` at the beginning of the line).*

### Step 4: Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 5: Configure Environment Variables
Copy the example environment configuration:
```bash
cp .env.example .env
```

### Step 6: Initialize Database & Seed Demonstration Data
Initialize the database schema and populate realistic demonstration records:
```bash
flask --app app init-db
flask --app app seed-db
```

### Step 7: Run the Flask Application
Start the local Flask development server:
```bash
python app.py
```
*(Alternatively, you can run: `flask --app app run --debug`)*

### Step 8: Access the Application in Your Browser
Open your browser (Safari, Chrome, or Firefox) and navigate to:
```
http://127.0.0.1:5000
```
Or:
```
http://localhost:5000
```

### Default Demonstration Accounts (For College Evaluation)
The database comes pre-seeded with sample demonstration tickets and two staff accounts:
- **Administrator Account:**
  - Username: `admin`
  - Password: `Admin@123`
- **Support Staff Account:**
  - Username: `support_agent`
  - Password: `Agent@123`

### Step 9: Stop the Server
When finished testing, return to the VS Code terminal and press:
<kbd>Ctrl</kbd> + <kbd>C</kbd>

---

## 7. Automated Testing

The project includes an automated test suite verifying all critical features. Run tests at any time using:

```bash
./venv/bin/python -m unittest -v tests/test_app.py
```

### Test Coverage Summary
- **Total Test Cases:** 18
- **Pass Rate:** 100% (18 Passed, 0 Failed, 0 Skipped)
- **Verified Areas:**
  - Database auto-initialization and seeding
  - Dashboard route loading and real-time metric computations
  - Ticket submission and validation (title lengths, email syntax, category whitelisting)
  - Unique ID auto-generation (`HD-XXXX`)
  - Ticket search by ID, title, and requester name
  - Multi-criteria filtering by status, category, and priority
  - Ticket details view and 404 error interception
  - Staff login, credential verification, and session logout
  - Server-side authorization (`@login_required`)
  - Status and priority update with automated audit logging
  - CSRF token interception on state-changing requests

---

## 8. Git & GitHub Submission Guide

Follow these commands to push the project to your personal GitHub repository:

### 1. Verify Git Status & Exclusions
Ensure private files (`venv/`, `.env`, and local `.db` files) are properly excluded:
```bash
git status
```
*(Check that `.env`, `venv/`, and `database/helpdesk.db` do **not** appear in the untracked list).*

### 2. Initialize Git Repository
```bash
git init
```

### 3. Stage & Commit Project Files
```bash
git add .
git commit -m "Initial commit: IT Help Desk Ticket Management System"
```

### 4. Link to Your GitHub Repository
1. Open [GitHub](https://github.com/) in your browser and click **New Repository**.
2. Name the repository: `it-helpdesk-ticket-system`.
3. Set the repository visibility to **Public**.
4. Leave "Add a README" **unchecked** (we already have a complete README).
5. Copy your new repository's URL and run:
```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/it-helpdesk-ticket-system.git
git push -u origin main
```

---

## 9. College Demonstration Sequence

When demonstrating the project to your college evaluation panel, follow this concise 4-step sequence:

1. **Dashboard Overview (1 minute):** Open `http://127.0.0.1:5000/`. Highlight the 5 live metric cards (Total, Open, In Progress, Resolved, High Priority) and point out that these numbers are computed dynamically from SQLite, not hardcoded.
2. **Submit a New Ticket (1 minute):** Click **New Ticket**. Intentionally submit a bad email or title to show error handling. Then enter valid details for a "Computer Engineering Lab 3" issue with High priority. Submit and show the auto-generated ID (e.g. `HD-1009`).
3. **Search & Filter (1 minute):** Navigate to **All Tickets**. Type `HD-1009` or `switch` into the search bar. Filter by Status = `Open` and Priority = `High` to demonstrate composite filtering.
4. **Staff Management & Audit Trail (1 minute):** Click **Staff Login** and sign in as `admin` (`Admin@123`). Open ticket `HD-1001`. Change the status from *Open* to *In Progress*, lower the priority, and enter an update note ("Inspected memory modules"). Save changes and show the newly appended entry in the **Activity & Progress Log** timeline.

---

## 10. Known Limitations & Future Scope

### Limitations
- **SQLite Concurrency:** SQLite is designed for light-to-moderate local write concurrency. High-traffic environments would benefit from migrating to PostgreSQL.
- **In-App Notifications:** Status updates are currently displayed within the web portal; external SMTP email alerts are not yet connected.
- **File Uploads:** Users cannot upload image screenshots or crash dump attachments directly.

### Future Scope (Version 2.0 Roadmap)
- **Automated Email Notifications:** Dispatch confirmation and resolution emails using Python `smtplib`.
- **Diagnostic File Attachments:** Enable secure image/log uploads with server-side MIME type verification.
- **SLA Countdown Timers:** Visual countdown badges for High-Priority incidents to ensure quick resolution.
- **AI-Powered Ticket Triage:** Automatically recommend categories and initial troubleshooting steps using NLP.

---

## 11. Author & Acknowledgements
- **Student Name:** [STUDENT FULL NAME]
- **Role:** Web and Software Applications Intern
- **Degree:** Bachelor of Engineering in Computer Engineering / Information Technology
- **Academic Year:** 2025–2026
- **Mentor:** [FACULTY GUIDE NAME]
