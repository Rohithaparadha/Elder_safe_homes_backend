# Elder-Safe Homes | Official Full-Stack Web Application

An official, secure, full-stack web application developed for **Elder-Safe Homes** based in Kukatpally, Hyderabad. This system replaces conventional static landing architectures with a reliable Python backend and persistent SQL data relational tables designed to seamlessly handle high-priority senior home safety assessment leads.

## 🚀 Key Features
- **Dynamic Flask Routing:** High-performance URL path resolving utilizing Python framework engines.
- **Persistent SQL Database:** Automated table instantiation using SQLite (`schema.sql`) to safely manage data entries.
- **Secure Lead Handling:** Native form parsing with embedded bot protections and backend validation logic.
- **Administrative Lead Dashboard:** An internal portal (`/admin/dashboard`) displaying structured customer data alongside precise auto-generated timestamps.
- **Responsive Architecture:** Customized UI utilizing clean modern typography and visual placeholders matching company design assets.

---

## 📂 Repository Layout
```text
elder_safe_homes/
│
├── app.py                 # Core Python Flask Backend 
├── database.db            # Local relational SQLite engine (Auto-created)
├── schema.sql             # SQL structural blueprints for database tables
├── requirements.txt       # Production cloud framework dependencies
│
├── static/                # Asset storage (Corporate layout visuals)
│   ├── IMG-20260520-WA0001.jpg
│   └── IMG-20260520-WA0002.jpg
│
└── templates/             # Python Jinja2 dynamic views
    ├── index.html         # Live customer homepage & booking module
    └── dashboard.html     # Secure internal corporate monitoring panel
