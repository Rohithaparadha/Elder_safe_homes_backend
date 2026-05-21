import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Force Render to use its internal /tmp directory with read/write permissions
DATABASE = '/tmp/database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Completely self-contained database table setup
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            service TEXT NOT NULL,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-request', methods=['POST'])
def submit_request():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        service = request.form.get('service')
        details = request.form.get('details')

        if not name or not phone or not service:
            return redirect(url_for('home', _anchor='contact'))

        try:
            init_db()
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO leads (name, phone, service, details) VALUES (?, ?, ?, ?)',
                (name, phone, service, details)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            pass
            
        return redirect(url_for('home', _anchor='contact'))

# Secure dashboard route using your password
@app.route('/admin/dashboard')
def dashboard():
    password = request.args.get('password')
    
    if password != "Safehome2026":
        return "<h1>Unauthorized Access</h1><p>You do not have permission to view corporate leads.</p>", 403

    init_db()

    conn = get_db_connection()
    leads = conn.execute('SELECT * FROM leads ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('dashboard.html', leads=leads)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
