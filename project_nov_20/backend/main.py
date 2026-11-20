from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector
from google import genai

load_dotenv()

app = FastAPI(title="AI Student Portal")

# -------------------- Middleware: CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # allow React frontend (localhost:5173)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- Gemini client --------------------
genai_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# -------------------- Database --------------------
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "12345"),
        database=os.getenv("DB_NAME", "student_portal"),
    )

# -------------------- Middleware: simple admin key auth --------------------
async def verify_admin_key(x_admin_key: str = Header(None)):
    expected = os.getenv("ADMIN_KEY", "admin123")
    if x_admin_key != expected:
        raise HTTPException(status_code=401, detail="Invalid or missing admin key")
    return x_admin_key

# -------------------- Models --------------------
class Student(BaseModel):
    name: str
    email: str
    course: str
    grade: str

class NotesRequest(BaseModel):
    notes: str

class LoginRequest(BaseModel):
    admin_key: str

# -------------------- Routes --------------------
@app.get("/")
def home():
    return {"message": "AI Student Portal API"}


@app.post("/login")
def login(req: LoginRequest):
    if req.admin_key == os.getenv("ADMIN_KEY", "admin123"):
        return {"ok": True, "token": "admin-token"}
    raise HTTPException(status_code=401, detail="Invalid admin key")


@app.get("/students")
def list_students():
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, course, grade FROM students ORDER BY id DESC")
        rows = cursor.fetchall()
        return [
            {"id": row[0], "name": row[1], "email": row[2], "course": row[3], "grade": row[4]}
            for row in rows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.post("/students", dependencies=[Depends(verify_admin_key)])
def add_student(student: Student):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, email, course, grade) VALUES (%s, %s, %s, %s)",
            (student.name, student.email, student.course, student.grade),
        )
        conn.commit()
        return {"message": "Student added successfully", "student": student.dict()}
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


# -------------------- Gemini AI routes --------------------
@app.post("/ai/summarize", dependencies=[Depends(verify_admin_key)])
def summarize(req: NotesRequest):
    try:
        response = genai_client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=(
                "Summarize the following study notes into simple bullet points. "
                "Keep it clear and student-friendly:\n\n" + req.notes
            ),
        )
        return {"summary": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ai/quiz", dependencies=[Depends(verify_admin_key)])
def quiz(req: NotesRequest):
    try:
        response = genai_client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=(
                "Create 5 multiple-choice quiz questions (with options A-D and the correct answer) "
                "from the following study notes:\n\n" + req.notes
            ),
        )
        return {"quiz": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
