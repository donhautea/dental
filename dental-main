import streamlit as st
import sqlite3
from datetime import date
import json
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Sidebar and title
st.set_page_config(layout="wide", page_title="Dental Clinic Client Form")
menu = st.sidebar.radio("Menu", ["Client Information Form"])

# Google Drive setup
def upload_to_drive(file_path, folder_id):
    creds_info = json.loads(st.secrets["google_drive"]["service_account_info"])
    credentials = service_account.Credentials.from_service_account_info(creds_info, scopes=["https://www.googleapis.com/auth/drive.file"])
    service = build("drive", "v3", credentials=credentials)

    file_metadata = {
        "name": os.path.basename(file_path),
        "parents": [folder_id]
    }
    media = MediaFileUpload(file_path, resumable=True)
    
    query = f"name='{os.path.basename(file_path)}' and '{folder_id}' in parents and trashed = false"
    existing_files = service.files().list(q=query, fields="files(id)").execute().get("files", [])
    
    if existing_files:
        file_id = existing_files[0]["id"]
        service.files().update(fileId=file_id, media_body=media).execute()
    else:
        service.files().create(body=file_metadata, media_body=media, fields="id").execute()

# SQLite setup
DB_NAME = "clients.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT, birth_date DATE, gender TEXT, contact TEXT, email TEXT,
            address TEXT, occupation TEXT, referred_by TEXT,
            medical_conditions TEXT, allergies TEXT, current_medications TEXT,
            last_dental_visit TEXT, reason_for_visit TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_client(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clients (
            full_name, birth_date, gender, contact, email, address, occupation, referred_by,
            medical_conditions, allergies, current_medications, last_dental_visit, reason_for_visit
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple(data.values()))
    conn.commit()
    conn.close()

    # Upload to Drive
    upload_to_drive(DB_NAME, st.secrets["google_drive"]["folder_id"])

# Run DB initializer
init_db()

# Display the form
if menu == "Client Information Form":
    st.title("🦷 Dental Clinic – Client Information Form")

    with st.form("client_form"):
        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input("Full Name")
            birth_date = st.date_input("Date of Birth", min_value=date(1900, 1, 1))
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            contact = st.text_input("Contact Number")
            email = st.text_input("Email")
            occupation = st.text_input("Occupation")

        with col2:
            address = st.text_area("Address")
            referred_by = st.text_input("Referred By")
            medical_conditions = st.text_area("Known Medical Conditions")
            allergies = st.text_area("Allergies")
            current_medications = st.text_area("Current Medications")
            last_dental_visit = st.text_input("Last Dental Visit (approx.)")
            reason_for_visit = st.text_area("Reason for Today’s Visit")

        submitted = st.form_submit_button("Submit")
        if submitted:
            client_data = {
                "full_name": full_name,
                "birth_date": birth_date.isoformat(),
                "gender": gender,
                "contact": contact,
                "email": email,
                "address": address,
                "occupation": occupation,
                "referred_by": referred_by,
                "medical_conditions": medical_conditions,
                "allergies": allergies,
                "current_medications": current_medications,
                "last_dental_visit": last_dental_visit,
                "reason_for_visit": reason_for_visit
            }
            save_client(client_data)
            st.success("✅ Client information saved and uploaded to Google Drive!")
