import sqlite3

try:
    conn = sqlite3.connect("test.db")
    print("SQLite Database Connected Successfully!")
    conn.close()
except sqlite3.Error as e:
    print("Error connecting to SQLite:", e)
