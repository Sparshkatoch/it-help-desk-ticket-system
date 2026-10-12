# INTERNSHIP PROJECT REPORT

# IT HELP DESK TICKET MANAGEMENT SYSTEM

---

### A Project Report Submitted in Partial Fulfillment of the Requirements for the Degree of
### BACHELOR OF ENGINEERING / TECHNOLOGY IN COMPUTER ENGINEERING / INFORMATION TECHNOLOGY

---

**Submitted by:**  
**[STUDENT FULL NAME]**  
**Roll No. / Enrollment ID:** [STUDENT ROLL NUMBER]  
**Academic Year:** 2025 – 2026  

**Under the Guidance of:**  
**Internal Academic Mentor:** [FACULTY GUIDE NAME & DESIGNATION]  
**External Industry Supervisor:** [INDUSTRY SUPERVISOR NAME & DESIGNATION]  

**Department of Computer Engineering / Information Technology**  
**[COLLEGE / UNIVERSITY NAME]**  
**[COLLEGE ADDRESS & LOCATION]**  

---

## 2. STUDENT DETAILS & INTERNSHIP DETAILS PLACEHOLDERS

- **Student Name:** [STUDENT FULL NAME]
- **Roll Number / PRN:** [STUDENT ROLL NUMBER]
- **Branch / Specialization:** Computer Engineering / Information Technology
- **Semester / Year:** 6th Semester / 3rd Year
- **Host Institution:** [COLLEGE / UNIVERSITY NAME]
- **Internship Organization:** [NAME OF INTERNSHIP COMPANY / FIRM]
- **Internship Role:** Web and Software Applications Intern
- **Internship Duration:** [START DATE] to [END DATE] (e.g., June 2025 – August 2025)
- **Mode of Internship:** [On-site / Hybrid / Remote]
- **Reporting Supervisor:** [SUPERVISOR NAME, DESIGNATION, COMPANY]

---

## 3. CERTIFICATE OF INTERNSHIP EVALUATION

*(Place on College / Department Letterhead)*

This is to certify that the project report entitled **“IT Help Desk Ticket Management System”** is a bonafide work carried out by **[STUDENT FULL NAME]** (Roll No: **[STUDENT ROLL NUMBER]**) in partial fulfillment of the academic requirements for the internship evaluation in the Bachelor of Engineering/Technology curriculum during the academic year 2025–2026.

The work described in this report has been carried out under our supervision and guidance, and to the best of our knowledge, represents genuine work completed by the student.

<br><br>

_____________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _____________________________  
**[FACULTY GUIDE NAME]** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **[HEAD OF DEPARTMENT]**  
Internal Project Mentor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Department of Computer Engineering  
[College Name] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [College Name]  

<br>

_____________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; _____________________________  
**External Examiner** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Date of Evaluation**  

---

## 4. DECLARATION

I, **[STUDENT FULL NAME]**, a student of Third Year Bachelor of Engineering in [Branch Name] at [College Name], hereby declare that the project titled **“IT Help Desk Ticket Management System”** submitted by me is an authentic record of my own work performed during my internship in **Web and Software Applications**.

I confirm that this project report has not been submitted previously to this or any other university for the award of any degree, diploma, or certificate. Any software libraries, algorithmic methodologies, and references utilized have been duly acknowledged.

<br>

**Date:** [Submission Date]  
**Place:** [City / Campus Location]  

<br>

_____________________________  
**[STUDENT FULL NAME]**  
Roll Number: [STUDENT ROLL NUMBER]  

---

## 5. ACKNOWLEDGEMENT

I express my deepest gratitude to my college management, principal, and faculty members of the Department of Computer Engineering/IT at **[COLLEGE NAME]** for providing the opportunity and institutional environment to undertake this internship project.

I am immensely grateful to my Internal Project Guide, **[FACULTY GUIDE NAME]**, for their continuous academic guidance, encouraging advice, and insightful feedback throughout the project lifecycle.

I also extend my sincere thanks to my industry supervisor, **[SUPERVISOR NAME]**, and colleagues at **[INTERNSHIP ORGANIZATION]** for their mentorship during my internship in Web and Software Applications. Their practical insights into production-level web design, modular software design, and defect tracking were invaluable.

Finally, I thank my family and friends for their unwavering encouragement and support during the preparation of this project and report.

---

## 6. ABSTRACT

In contemporary educational institutions, colleges, and business organizations, reliable Information Technology (IT) infrastructure is critical for day-to-day operations. However, technical complaints regarding lab workstations, network connectivity, software compiler packages, ERP login access, and peripheral devices are frequently reported through unstructured communication channels—such as casual verbal complaints, phone calls, or unmonitored email inboxes. This lack of centralized tracking leads to delayed issue resolution, lost requests, lack of technician accountability, and an absence of operational metrics.

To overcome these challenges, this project presents the **IT Help Desk Ticket Management System**, a lightweight, robust, and beginner-friendly full-stack web application developed using **Python with Flask**, an **SQLite relational database**, and a clean **HTML5/CSS3/JavaScript** frontend. The application enables users to log support complaints across 6 distinct IT categories, assigns auto-generated human-readable ticket IDs (e.g., `HD-1001`), and provides an operational dashboard displaying dynamic statistics calculated from live database records. IT support personnel can authenticate using secure PBKDF2 password hashing, filter ticket queues across status, category, and priority parameters, transition ticket lifecycles, and maintain an activity log. The application implements parameter-driven SQL queries, Cross-Site Request Forgery (CSRF) mitigation, secure session management, and automated test coverage. The entire software runs locally on macOS without relying on paid APIs or external database hosting, providing a solid foundation for academic evaluation and institutional adoption.

---

## 7. TABLE OF CONTENTS

1. Cover Page
2. Student Details and Internship Details Placeholders
3. Certificate Placeholder
4. Declaration
5. Acknowledgement
6. Abstract
7. Table of Contents
8. Introduction
9. Problem Statement
10. Objectives
11. Existing System and Its Limitations
12. Proposed System
13. Software and Hardware Requirements
14. Technology Stack
15. System Architecture
16. Functional and Non-Functional Requirements
17. Use-Case Descriptions
18. Data Flow Diagram (DFD)
19. Database Schema and ER Diagram
20. Module Descriptions
21. Implementation Details
22. Testing and Test Cases
23. Screenshots with Captions and Placeholders
24. Results and Discussion
25. Limitations
26. Future Scope
27. Conclusion
28. References

---

## 8. INTRODUCTION

Modern organizations operate dozens of computer laboratories, administrative servers, network switches, and shared peripheral devices. Throughout typical daily operations, faculty members, administrative staff, and students encounter technical disruptions: operating system crashes, Wi-Fi authentication timeouts, laboratory printer jams, compiler permission errors, and student portal credential lockouts.

When an organization lacks a systematic incident management framework, technical issues are reported haphazardly. Support technicians have no means of prioritizing critical infrastructure failures over minor cosmetic questions, leading to extended downtime. 

The **IT Help Desk Ticket Management System** addresses this problem by digitizing and automating the complaint management workflow. Built during my internship in **Web and Software Applications**, this application establishes a transparent, audited channel connecting end-users directly with technical support teams.

---

## 9. PROBLEM STATEMENT

Manual and ad-hoc IT complaint management methods within academic and institutional environments suffer from the following core problems:
1. **Loss of Issue Traceability:** Complaints submitted verbally or via unstructured emails get misplaced or forgotten without a permanent record.
2. **Lack of Priority Triage:** Technicians cannot distinguish emergency incidents (such as campus-wide Wi-Fi outages) from routine requests (such as software license questions).
3. **Absence of Accountability:** Without timestamped ownership and status change logs, support managers cannot verify when an issue was addressed or who worked on it.
4. **No Operational Analytics:** Administrators have no visibility into recurring hardware failures, high-failure laboratory equipment, or technician workload metrics.

---

## 10. OBJECTIVES

The primary objectives of the IT Help Desk Ticket Management System are:
- **Centralize Complaint Ingestion:** Provide an intuitive, accessible web form for reporting issues across all IT domains.
- **Automated Identifier Generation:** Generate human-friendly, sequential ticket identifiers (e.g., `HD-1001`) for clear tracking.
- **Real-Time Operational Dashboard:** Aggregate database records into key performance metrics (Total, Open, In Progress, Resolved, and High-Priority tickets).
- **Multi-Criteria Search & Filtering:** Enable support technicians to rapidly locate records using query text and structured filter dropdowns.
- **Role-Based Lifecycle Tracking:** Provide authenticated support staff with controls to update ticket status, adjust priority, and append activity logs.
- **Security & Integrity:** Implement defense against SQL Injection, Cross-Site Request Forgery (CSRF), and unauthorized route tampering.
- **Cost-Free Local Execution:** Ensure complete functionality on macOS using VS Code, Python virtual environments, and SQLite without paid subscriptions.

---

## 11. EXISTING SYSTEM AND ITS LIMITATIONS

In many departments and small institutions, technical support relies on one of three existing methods:

### 1. Verbal & Physical Register Logs
Users report issues in person at the IT department, where complaints are noted in a paper logbook.
- **Limitations:** Registers get misplaced; physical presence is required; search is impossible; no notification mechanism exists; handwriting is ambiguous.

### 2. General Email Inboxes
Users send an email to an IT email address (`helpdesk@institution.edu`).
- **Limitations:** High email volume leads to overlooked emails; multiple technicians may work on the same issue simultaneously; no structured categorization or priority metadata; reporting metrics cannot be calculated automatically.

### 3. Commercial Enterprise Helpdesk Suites (e.g., ServiceNow, Zendesk, Jira Service Desk)
- **Limitations:** Prohibitive software license costs; complex enterprise setup requiring dedicated database servers; steep learning curve for college staff and students.

---

## 12. PROPOSED SYSTEM

The proposed **IT Help Desk Ticket Management System** provides a lightweight, focused, and custom-built solution tailored for departmental and campus environments:
- **Zero Cost & Open Source:** Utilizes Python, Flask, and SQLite with zero external license fees.
- **Structured Categorization:** Organizes complaints into 6 explicit categories: Software errors, Computer or laptop issues, Internet and network problems, Login and account access, Printer and peripheral issues, and Other technical problems.
- **Dynamic Database Metrics:** Dashboard displays real-time statistics queried directly via SQL aggregation functions.
- **Two-Tier Access Model:** Public users can log issues and track ticket statuses; authenticated staff members have protected access to lifecycle management and audit logging.
- **Audited Activity Timeline:** Every update and technician observation is recorded chronologically in an associated notes table.

---

## 13. SOFTWARE AND HARDWARE REQUIREMENTS

### Software Requirements
- **Operating System:** macOS (macOS Monterey / Ventura / Sonoma / Sequoia)
- **Code Editor / IDE:** Visual Studio Code (VS Code) with Python Extension
- **Backend Runtime:** Python 3.10+ (tested and verified on Python 3.14)
- **Web Framework:** Flask 3.1+ (Python WSGI Micro-framework)
- **Database Engine:** SQLite 3 (built into standard Python runtime)
- **Frontend Technologies:** HTML5, CSS3, Vanilla JavaScript (ES6+)
- **Version Control:** Git 2.30+ and GitHub
- **Package Management:** Python Virtual Environment (`venv`) and `pip`

### Hardware Requirements
- **Processor:** Apple Silicon (M1/M2/M3/M4) or Intel Core i5/i7 Processor
- **RAM:** 4 GB minimum (8 GB recommended for simultaneous IDE & browser execution)
- **Storage:** 500 MB free hard disk space
- **Display:** 1366 x 768 minimum display resolution (Retina display supported)
- **Network Interface:** Local loopback interface (`127.0.0.1` / `localhost`)

---

## 14. TECHNOLOGY STACK

| Layer | Technology | Justification |
| :--- | :--- | :--- |
| **Frontend - Structure** | HTML5 | Semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<footer>`), native form input validation, accessibility. |
| **Frontend - Styling** | CSS3 (Vanilla) | Custom responsive layout using CSS Variables, modern Flexbox, and CSS Grid. Zero external bloat; fast local rendering. |
| **Frontend - Interactivity** | JavaScript (ES6+) | Mobile navigation toggle, auto-dismissing toast alerts, and status change confirmation dialogs. |
| **Backend Framework** | Python & Flask | Clean WSGI architecture, declarative routing, lightweight footprint, and intuitive template rendering via Jinja2. |
| **Database** | SQLite 3 | Embedded, zero-configuration relational database engine with transactional ACID properties stored in a single local file. |
| **Security Modules** | Werkzeug & Secrets | Secure PBKDF2 password hashing with cryptographic salt; random token generation for session CSRF protection. |
| **Testing** | Python `unittest` | Automated test runner validating routes, database queries, access control, and error handling. |

---

## 15. SYSTEM ARCHITECTURE

The application implements the **Model-View-Controller (MVC)** architectural pattern:

```
+--------------------------------------------------------------------------+
|                            USER AGENT (BROWSER)                          |
|  - HTML5 Responsive Views (Dashboard, Ticket Queue, Creation Form)       |
|  - Custom CSS3 Styling & Vanilla JavaScript DOM Interactions             |
+------------------------------------+-------------------------------------+
                                     | HTTP Requests (GET / POST)
                                     v
+--------------------------------------------------------------------------+
|                          FLASK APPLICATION LAYER                         |
|  - WSGI Application (app.py)                                             |
|  - Route Dispatcher & Controllers                                        |
|  - Input Validation & Sanitization Engine                                |
|  - CSRF Token Interceptor & @login_required Decorator                     |
|  - Jinja2 Template Engine with Custom Filters                            |
+------------------------------------+-------------------------------------+
                                     | Parameterized SQL Queries
                                     v
+--------------------------------------------------------------------------+
|                         DATABASE LAYER (SQLITE3)                         |
|  - helpdesk.db (Physical SQLite File)                                    |
|  - Tables: users, tickets, ticket_notes                                  |
|  - Relational Foreign Keys (ON DELETE CASCADE)                           |
|  - Performance B-Tree Indexes on ticket_id, status, priority             |
+--------------------------------------------------------------------------+
```

---

## 16. FUNCTIONAL AND NON-FUNCTIONAL REQUIREMENTS

### Functional Requirements
1. **User Ticket Registration:** Public or departmental users must be able to submit a complaint specifying Title, Description, Requester Name, Email, Category, Priority, and Department.
2. **Unique Identifier Assignment:** The system must automatically assign a unique, sequential ticket ID (e.g., `HD-1001`) upon creation.
3. **Live Statistical Dashboard:** The dashboard must calculate and display Total, Open, In Progress, Resolved, and High-Priority tickets from live database counts.
4. **Search Functionality:** Users must be able to search for tickets by Ticket ID, Title, or Requester Name.
5. **Filtering Capability:** Users must be able to filter tickets by Status, Category, and Priority.
6. **Authentication & Authorization:** Staff members must authenticate using a secure login form. Protected routes must block unauthenticated updates.
7. **Lifecycle Updates & Audit Logging:** Authenticated staff must be able to transition ticket statuses and record technician observation notes.

### Non-Functional Requirements
1. **Performance:** Sub-second response times on local execution; SQL indexes on query columns.
2. **Security:** Defense against SQL Injection via parameterized queries; CSRF mitigation; password hashing using PBKDF2.
3. **Usability & UX:** Responsive layout adapting across desktop and mobile screens; clear visual badge indicators for priority and status.
4. **Maintainability:** Modular project directory structure separating templates, database scripts, static assets, and tests.
5. **Reliability:** Graceful error handling for missing tickets (404) and server anomalies (500) without crashing.

---

## 17. USE-CASE DESCRIPTIONS

### Use Case 1: Report Technical Incident (End User)
- **Actor:** Student, Faculty Member, or Staff Member
- **Pre-conditions:** Web portal is accessible in browser.
- **Main Flow:**
  1. User navigates to `/tickets/new`.
  2. User fills out the required incident details and selects category and urgency.
  3. User submits the form.
  4. System validates inputs and assigns an incremental Ticket ID.
  5. System persists the record and redirects to the Ticket Details page with a success message.
- **Post-conditions:** Ticket is stored with status `Open`.

### Use Case 2: Triage & Update Ticket (Support Staff)
- **Actor:** Authenticated Support Staff / Administrator
- **Pre-conditions:** Technician is logged in via `/login`.
- **Main Flow:**
  1. Staff navigates to `/tickets` and inspects the queue using status or priority filters.
  2. Staff opens the target ticket details view (`/tickets/<ticket_id>`).
  3. Staff updates the status to `In Progress` or `Resolved` and enters a diagnostic note.
  4. System updates the ticket record and inserts an audit log entry in `ticket_notes`.
- **Post-conditions:** Ticket status is updated and timestamp is refreshed.

---

## 18. DATA FLOW DIAGRAM (DFD)

### Level 0 DFD (Context Diagram)

```
             +-----------------------+
             |   End User / Staff    |
             +-----------+-----------+
                         |
      1. Submit Ticket   |   2. View Ticket Status & Dashboard
                         v
             +---------------------------------------+
             |                                       |
             |  IT Help Desk Ticket Management System|
             |               (Flask App)             |
             |                                       |
             +-------------------+-------------------+
                                 |
                 3. Query & Store| 4. Return Records
                                 v
             +---------------------------------------+
             |         SQLite Database               |
             |          (helpdesk.db)                |
             +---------------------------------------+
```

### Level 1 DFD (Decomposed Process Diagram)

```
 [User] ---> (Process 1.0: Validate & Create Ticket) ---> [DB: tickets]
                                                                |
 [User/Staff] ---> (Process 2.0: Query Dashboard & Queue) <-----+
                                                                |
 [Staff] ---> (Process 3.0: Authenticate Credentials) ---> [DB: users]
                                                                |
 [Staff] ---> (Process 4.0: Update Status & Log Notes) ---> [DB: ticket_notes]
```

---

## 19. DATABASE SCHEMA AND ER DIAGRAM

### Entity-Relationship (ER) Diagram

```
+---------------------+             1 : N             +---------------------+
|        USERS        |------------------------------>|    TICKET_NOTES     |
+---------------------+                               +---------------------+
| PK  id              |                               | PK  id              |
|     username        |                               | FK  ticket_id       |
|     email           |                               |     author          |
|     password_hash   |                               |     note            |
|     role            |                               |     created_at      |
|     created_at      |                               +----------+----------+
+---------------------+                                          |
                                                                 | N : 1
                                                                 v
                                                      +---------------------+
                                                      |       TICKETS       |
                                                      +---------------------+
                                                      | PK  id              |
                                                      |     ticket_id (UQ)  |
                                                      |     title           |
                                                      |     description     |
                                                      |     requester_name  |
                                                      |     requester_email |
                                                      |     category        |
                                                      |     priority        |
                                                      |     status          |
                                                      |     department      |
                                                      |     created_at      |
                                                      |     updated_at      |
                                                      +---------------------+
```

### Table Definitions & Constraints
1. **`users` Table:**
   - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `username`: TEXT UNIQUE NOT NULL
   - `email`: TEXT UNIQUE NOT NULL
   - `password_hash`: TEXT NOT NULL
   - `role`: TEXT NOT NULL DEFAULT 'staff' CHECK (role IN ('admin', 'staff'))
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

2. **`tickets` Table:**
   - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `ticket_id`: TEXT UNIQUE NOT NULL (Indexed)
   - `title`: TEXT NOT NULL
   - `description`: TEXT NOT NULL
   - `requester_name`: TEXT NOT NULL
   - `requester_email`: TEXT NOT NULL
   - `category`: TEXT NOT NULL CHECK (category IN ('Software errors', 'Computer or laptop issues', 'Internet and network problems', 'Login and account access', 'Printer and peripheral issues', 'Other technical problems'))
   - `priority`: TEXT NOT NULL CHECK (priority IN ('Low', 'Medium', 'High'))
   - `status`: TEXT NOT NULL DEFAULT 'Open' CHECK (status IN ('Open', 'In Progress', 'Resolved'))
   - `department`: TEXT
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   - `updated_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

3. **`ticket_notes` Table:**
   - `id`: INTEGER PRIMARY KEY AUTOINCREMENT
   - `ticket_id`: INTEGER NOT NULL REFERENCES tickets(id) ON DELETE CASCADE
   - `author`: TEXT NOT NULL
   - `note`: TEXT NOT NULL
   - `created_at`: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

---

## 20. MODULE DESCRIPTIONS

### 1. Dashboard Module (`dashboard()`)
Responsible for calculating real-time aggregated metrics. Executes counting queries for total tickets, open tickets, in-progress tickets, resolved tickets, and high-priority tickets. Also groups records by category and fetches the latest 6 tickets for rapid inspection.

### 2. Ticket Submission Module (`create_ticket()`)
Presents the incident submission form and enforces validation rules: checks title length (5–120 characters), description depth (min 10 characters), email regex syntax, and verifies that category and priority belong to predefined valid sets. Generates the next sequential ticket ID.

### 3. Ticket Queue & Search Module (`tickets()`)
Renders the complete table of support tickets. Supports text search matching Ticket ID, Title, and Requester Name, as well as multi-criteria filtering by Status, Category, and Priority.

### 4. Ticket Details & Management Module (`ticket_details()`, `update_ticket_status()`, `add_ticket_note()`)
Displays the complete ticket attributes, full description, and chronological activity timeline. Enforces staff authentication via `@login_required` before allowing changes to ticket status or priority, and logs all changes to `ticket_notes`.

### 5. Authentication & Access Control Module (`login()`, `logout()`)
Manages staff authentication using Werkzeug password hashing. Generates session cookies on successful verification and clears session state on logout.

---

## 21. IMPLEMENTATION DETAILS

### Unique Ticket ID Generator Algorithm
```python
def generate_ticket_id(db):
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
    cursor.execute("SELECT COUNT(*) as cnt FROM tickets")
    count = cursor.fetchone()['cnt']
    return f"HD-{1001 + count}"
```

### Server-Side CSRF Token Verification
```python
def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = secrets.token_hex(32)
    return session['_csrf_token']

@app.before_request
def csrf_protect():
    if not app.config.get('CSRF_ENABLED', True):
        return
    if request.method in ('POST', 'PUT', 'DELETE', 'PATCH'):
        token = request.form.get('csrf_token') or request.headers.get('X-CSRFToken')
        session_token = session.get('_csrf_token')
        if not session_token or not token or token != session_token:
            flash('Security token validation failed. Please refresh the page and try again.', 'error')
            abort(403)
```

---

## 22. TESTING AND TEST CASES

The application was tested through automated unit and integration tests using Python's `unittest` framework. An isolated temporary SQLite database was used for every test run to guarantee test independence.

### Summary of Automated Test Results
- **Total Tests Executed:** 18
- **Tests Passed:** 18 (100%)
- **Failures / Errors:** 0
- **Execution Time:** ~1.6 seconds

*(Refer to `docs/test_cases.md` for the full 20-point test specification matrix.)*

---

## 23. SCREENSHOTS WITH CAPTIONS AND PLACEHOLDERS

*(During viva demonstration, capture screenshots from your running browser and insert them below)*

### Screenshot 1: IT Operations Dashboard
`[INSERT SCREENSHOT OF DASHBOARD: Showing metrics cards, category progress meters, and recent tickets table]`  
*Caption: Figure 23.1 – Real-time IT Help Desk Dashboard with dynamic SQLite metrics.*

### Screenshot 2: Submit New IT Ticket Form
`[INSERT SCREENSHOT OF CREATE TICKET PAGE: Showing validation fields and priority radio cards]`  
*Caption: Figure 23.2 – Incident registration form with input validation and guidance sidebar.*

### Screenshot 3: Ticket Queue with Search & Multi-Filters
`[INSERT SCREENSHOT OF TICKETS LISTING: Showing search results and filtered rows]`  
*Caption: Figure 23.3 – Searchable and filterable ticket queue with priority badges.*

### Screenshot 4: Ticket Details & Staff Controls View
`[INSERT SCREENSHOT OF TICKET DETAILS: Showing issue description, activity log, and staff update controls]`  
*Caption: Figure 23.4 – Detailed ticket inspection view with timeline log and status controls.*

### Screenshot 5: Staff & Admin Login Portal
`[INSERT SCREENSHOT OF LOGIN PAGE: Showing login card and evaluation credentials notice]`  
*Caption: Figure 23.5 – Secure staff authentication portal with hashed credential validation.*

---

## 24. RESULTS AND DISCUSSION

The implementation met all functional and non-functional goals set forth for the internship evaluation:
1. **Accurate Operational Tracking:** All dashboard statistics are computed directly from live database records, eliminating static or placeholder values.
2. **Defensive Validation:** Both client and server-side validation protect the database from malformed strings or invalid categories.
3. **Responsive Presentation:** The interface adapts smoothly to MacBook and mobile screens without horizontal layout breaking.
4. **Lightweight Footprint:** The application starts instantly, requires zero paid cloud infrastructure, and stores all data in a reliable, single-file SQLite database.

---

## 25. LIMITATIONS

1. **Database Write Concurrency:** SQLite utilizes file-level locking during write operations, making it unsuitable for thousands of concurrent write transactions.
2. **In-App Notifications Only:** The current implementation displays status updates in-app; external SMTP email or SMS notifications are not yet connected.
3. **No File Attachments:** Users cannot upload image screenshots or hardware crash logs directly with their ticket submission.

---

## 26. FUTURE SCOPE

For future iterations (Version 2.0), the following enhancements are planned:
1. **Automated Email Notifications:** Integrate Python's `smtplib` to send automated email confirmations when tickets are submitted and resolved.
2. **File Upload Support:** Add secure file upload functionality allowing users to attach diagnostic logs and screenshots.
3. **SLA (Service Level Agreement) Timers:** Implement countdown timers on high-priority tickets to ensure prompt resolution within designated institutional windows.
4. **AI-Powered Ticket Triage:** Integrate Natural Language Processing (NLP) to auto-detect complaint categories and suggest initial troubleshooting steps.

---

## 27. CONCLUSION

The **IT Help Desk Ticket Management System** successfully addresses the operational bottlenecks of manual and email-based technical complaint tracking. Developed using Python, Flask, SQLite, HTML5, CSS3, and JavaScript, the application delivers a complete, secure, and beginner-friendly solution that fulfills all academic internship project requirements. The project demonstrates the practical application of core software engineering principles—including MVC architecture, relational database design, defensive validation, CSRF protection, and automated testing—providing a dependable system ready for college evaluation.

---

## 28. REFERENCES

1. Grinberg, Miguel. *Flask Web Development: Developing Web Applications with Python*. O'Reilly Media, 2nd Edition.
2. SQLite Development Team. *SQLite Documentation and Architecture Reference*. Available at: https://www.sqlite.org/docs.html
3. Mozilla Developer Network (MDN). *HTML5, CSS3, and JavaScript Web Standards Guide*. Available at: https://developer.mozilla.org/
4. Werkzeug Security & Utilities Documentation. *Password Hashing and Secure Cookie Handling*. Available at: https://werkzeug.palletsprojects.com/
5. Python Software Foundation. *Python 3 Standard Library: unittest & sqlite3 Modules*. Available at: https://docs.python.org/3/
