import sqlite3

def get_connection(db_path='dental_clinic.db'):
    return sqlite3.connect(db_path, check_same_thread=False)