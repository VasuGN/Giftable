
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Student Delete")

students = [
    {
        "id": str(uuid4()),
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    },
    {
        "id": str(uuid4()),
        "name": "Sneha",
        "age": 22,
        "course": "FastAPI"
    },
    {
        "id": str(uuid4()),
        "name": "Kiran",
        "age": 23,
        "course": "JavaScript"
    }
]

@app.get("/students")
def get_students():
    return students

@app.delete("/students/{student_id}")
def delete_student(student_id: str):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully"
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
