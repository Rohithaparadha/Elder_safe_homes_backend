import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24) # Secure key for temporary session alerts
DATABASE = 'database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Database Initialization
def init_db():
    if not os.path.exists(DATABASE):
        conn = get_db_connection()
        with app.open_resource('schema.sql', mode='r') as f:
            conn.cursor().executescript(f.read())
        conn.commit()
        conn.close()

@app.route('/')
def home():
    return render_template('index.html')

# POST handler for incoming leads
@app.route('/submit-request', methods=['POST'])
def submit_request():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        service = request.form.get('service')
        details = request.form.get('details')

        if not name or not phone or not service:
            flash("Please fill out all required fields.", "error")
            return redirect(url_for('home', _anchor='contact'))

        try:
            conn = get_db_connection()
            conn.execute(
                'INSERT INTO leads (name, phone, service, details) VALUES (?, ?, ?, ?)',
                (name, phone, service, details)
            )
            conn.commit()
            conn.close()
            flash("Your request has been successfully submitted! Our Hyderabad team will call you shortly.", "success")
        except Exception as e:
            flash("An error occurred while saving your request. Please call us directly.", "error")
            
        return redirect(url_for('home', _anchor='contact'))

# Admin Dashboard to view leads collected securely
@app.route('/admin/dashboard')
def dashboard():
    conn = get_db_connection()
    leads = conn.execute('SELECT * FROM leads ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('dashboard.html', leads=leads)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)