def record_payment(conn, patient_id, amount, method, insurance, billing_date):
    c = conn.cursor()
    c.execute("INSERT INTO billing (patient_id, amount, method, insurance, billing_date) VALUES (?, ?, ?, ?, ?)",
              (patient_id, amount, method, insurance, billing_date))
    conn.commit()