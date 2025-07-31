from datetime import datetime

def log_action(conn, username, action, module, details=''):
    c = conn.cursor()
    c.execute("INSERT INTO audit_logs (username, action, module, details, timestamp) VALUES (?, ?, ?, ?, ?)",
              (username, action, module, details, datetime.now().isoformat()))
    conn.commit()