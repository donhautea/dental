def add_medical_history(conn, patient_id, conditions, allergies, medications):
    c = conn.cursor()
    c.execute("INSERT INTO medical_history (patient_id, conditions, allergies, medications) VALUES (?, ?, ?, ?)",
              (patient_id, conditions, allergies, medications))
    conn.commit()