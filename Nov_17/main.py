from fastapi import FastAPI, HTTPException
import pymysql

app = FastAPI()


def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="12345",
        database="nov_17",
    )


@app.get("/")
def home():
    conn = get_connection()
    try:
        return {"message": "connection successful"}
    finally:
        conn.close()


@app.post("/insert")
def insert_data(name: str, age: int, address: str):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, age, address) VALUES (%s, %s, %s)",
            (name, age, address),
        )
        conn.commit()
        return {
            "message": "data inserted successfully",
            "data": {"name": name, "age": age, "address": address},
        }
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.get("/students")
def list_students():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name, age, address FROM students")
        rows = cursor.fetchall()
        return [
            {"name": row[0], "age": row[1], "address": row[2]}
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
