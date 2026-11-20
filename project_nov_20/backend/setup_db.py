import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", "12345"),
)
cursor = conn.cursor()

cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME', 'student_portal')}")
cursor.execute(f"USE {os.getenv('DB_NAME', 'student_portal')}")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    course VARCHAR(100),
    grade VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
print("Database and table ready.")
cursor.close()
conn.close()
