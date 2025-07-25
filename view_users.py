import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

try:
    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()

    print("Existing users:")
    for row in rows:
        print(row)
except sqlite3.OperationalError as e:
    print("Table may not exist yet:", e)

conn.close()
