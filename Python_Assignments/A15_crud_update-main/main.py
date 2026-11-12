
from pathlib import Path
from typing import List
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Student Update")

class Student(BaseModel):
    name: str
    age: int
    course: str

students = [
    {
        "id": str(uuid4()),
        "name": "Arun",
        "age": 22,
        "course": "Python"
    },
    {
        "id": str(uuid4()),
        "name": "Priya",
        "age": 23,
        "course": "FastAPI"
    }
]

@app.get("/students")
def get_students():
    return students

@app.put("/students/{student_id}")
def update_student(student_id: str, updated_student: Student):

    for index, student in enumerate(students):

        if student["id"] == student_id:

            students[index] = {
                "id": student_id,
                **updated_student.model_dump()
            }

            return {
                "message": "Student updated successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )

html_path = Path(__file__).parent

app.mount(
    "/",
    StaticFiles(directory=html_path, html=True),
    name="static"
)
