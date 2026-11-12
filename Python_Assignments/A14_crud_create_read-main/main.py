
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Student Create and Read")

class Student(BaseModel):
    name: str
    age: int
    course: str

students = []

@app.post("/students")
def create_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully"}

@app.get("/students")
def get_students():
    return students

html_path = Path(__file__).parent

app.mount(
    "/",
    StaticFiles(directory=html_path, html=True),
    name="static"
)
