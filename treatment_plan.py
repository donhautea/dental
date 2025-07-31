def create_treatment_plan(conn, patient_id, procedures, est_cost, created_at):
    c = conn.cursor()
    c.execute("INSERT INTO treatment_plans (patient_id, procedures, est_cost, created_at) VALUES (?, ?, ?, ?)",
              (patient_id, procedures, est_cost, created_at))
    conn.commit()