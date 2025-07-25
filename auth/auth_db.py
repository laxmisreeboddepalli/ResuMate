import sqlite3
import hashlib

def get_connection():
    return sqlite3.connect("users.db", check_same_thread=False)

def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def add_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        email = email.lower().strip()
        hashed_pw = hash_password(password)

        # Debug print to trace insert
        print(f"[DEBUG] Trying to insert user with email: {email}")

        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                       (name, email, hashed_pw))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f"[DEBUG] Email already exists in DB: {email}")
        raise ValueError("Email already exists.")
    finally:
        conn.close()

def verify_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    email = email.lower().strip()
    hashed_pw = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?",
                   (email, hashed_pw))
    result = cursor.fetchone()
    conn.close()
    return result
