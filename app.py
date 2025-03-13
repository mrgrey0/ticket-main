from flask import Flask, render_template, request
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('tickets.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    ticket_id = None
    warning = None
    if request.method == 'POST':
        email = request.form['email']
        ip_address = request.remote_addr
        conn = get_db_connection()
        c = conn.cursor()

        # Check if the user already has a valid ticket
        c.execute('''
            SELECT * FROM tickets WHERE (email = ? OR ip_address = ?) AND expiry_time > ?
        ''', (email, ip_address, datetime.now()))
        existing_ticket = c.fetchone()

        if existing_ticket:
            ticket_id = existing_ticket['ticket_id']
            warning = "You already have a valid ticket."
        else:
            # Find an unassigned ticket ID
            c.execute('''
                SELECT * FROM ticket_ids WHERE assigned = 0 ORDER BY id LIMIT 1
            ''')
            available_ticket = c.fetchone()

            if available_ticket:
                ticket_id = available_ticket['ticket_id']
                expiry_time = datetime.now() + timedelta(minutes=5)  # Set expiry time to 5 minutes for testing

                # Assign the ticket to the user
                c.execute('''
                    INSERT INTO tickets (email, ip_address, ticket_id, expiry_time) VALUES (?, ?, ?, ?)
                ''', (email, ip_address, ticket_id, expiry_time))
                c.execute('''
                    UPDATE ticket_ids SET assigned = 1 WHERE id = ?
                ''', (available_ticket['id'],))
                conn.commit()
            else:
                warning = "No tickets available."

        conn.close()
    return render_template('index.html', ticket_id=ticket_id, warning=warning)

if __name__ == '__main__':
    app.run(debug=True)