def schedule_appointment(conn, patient_id, datetime, purpose, status='Scheduled'):
    c = conn.cursor()
    c.execute("INSERT INTO appointments (patient_id, appointment_date, purpose, status) VALUES (?, ?, ?, ?)",
              (patient_id, datetime, purpose, status))
    conn.commit()

def get_appointments(conn, date_filter=None):
    c = conn.cursor()
    if date_filter:
        c.execute("SELECT * FROM appointments WHERE appointment_date=?", (date_filter,))
    else:
        c.execute("SELECT * FROM appointments")
    return c.fetchall()