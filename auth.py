from fastapi import FastAPI, HTTPException
import sqlite3
from passlib.context import CryptContext

app = FastAPI()

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Database Connection Function
def get_db_connection():
    conn = sqlite3.connect("library.db")
    conn.row_factory = sqlite3.Row
    return conn

# User Signup
@app.post("/signup")
def signup(username: str, email: str, password: str):
    hashed_password = pwd_context.hash(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
                       (username, email, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username or Email already exists")
    finally:
        conn.close()
    return {"message": "User created successfully"}

# User Login
@app.post("/login")
def login(email: str, password: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    
    if user and pwd_context.verify(password, user["password"]):
        return {"message": "Login successful", "username": user["username"]}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

# Run API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
