import sqlite3

# Database connection
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create Users Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT DEFAULT 'user'  -- 'admin' or 'user'
    )
''')

# Create Books Table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        category TEXT NOT NULL,
        available INTEGER DEFAULT 1  -- 1 = Available, 0 = Borrowed
    )
''')

conn.commit()
conn.close()
