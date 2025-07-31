def add_progress_note(conn, patient_id, visit_date, notes, procedure_done):
    c = conn.cursor()
    c.execute("INSERT INTO progress_notes (patient_id, visit_date, notes, procedure_done) VALUES (?, ?, ?, ?)",
              (patient_id, visit_date, notes, procedure_done))
    conn.commit()