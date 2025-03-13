import sqlite3

def init_db():
    conn = sqlite3.connect('tickets.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            ip_address TEXT NOT NULL,
            ticket_id TEXT NOT NULL,
            expiry_time DATETIME NOT NULL
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS ticket_ids (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_id TEXT NOT NULL,
            assigned BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    
    # Populate the ticket_ids table with random ticket data
    for i in range(1, 101):  # Create 100 tickets
        ticket_id = f"TICKET-{i:03d}"
        c.execute('''
            INSERT INTO ticket_ids (ticket_id, assigned) VALUES (?, 0)
        ''', (ticket_id,))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()