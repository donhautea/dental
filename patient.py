def add_patient(conn, patient_data):
    c = conn.cursor()
    c.execute("INSERT INTO patients (name, birthdate, contact, address, email) VALUES (?, ?, ?, ?, ?)",
              (patient_data['name'], patient_data['birthdate'], patient_data['contact'], patient_data['address'], patient_data['email']))
    conn.commit()

def get_patient(conn, patient_id):
    c = conn.cursor()
    c.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    return c.fetchone()

def update_patient(conn, patient_id, updated_data):
    c = conn.cursor()
    c.execute("UPDATE patients SET name=?, birthdate=?, contact=?, address=?, email=? WHERE id=?",
              (updated_data['name'], updated_data['birthdate'], updated_data['contact'], updated_data['address'], updated_data['email'], patient_id))
    conn.commit()