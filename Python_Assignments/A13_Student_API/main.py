
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(
    title="Student Performance API",
    description="Assignment 13 - Student Management using GET routes",
    version="1.0.0"
)


# Student Model
class StudentModel(BaseModel):
    id: int
    name: str
    email: str
    course: str
    marks: float = Field(ge=0, le=100)
    attendance: float = Field(ge=0, le=100)


# Sample Student Data
students: List[StudentModel] = [
    StudentModel(id=1, name="Vasu G N", email="vasu@gmail.com",
                 course="Python", marks=85, attendance=90),

    StudentModel(id=2, name="Vinay Raj", email="vraj@gmail.com",
                 course="Data Science", marks=92, attendance=95),

    StudentModel(id=3, name="Karthik R", email="karthik@gmail.com",
                 course="Python", marks=45, attendance=70),

    StudentModel(id=4, name="Divya S", email="divya@gmail.com",
                 course="Web Development", marks=78, attendance=88),

    StudentModel(id=5, name="Manoj P", email="manoj@gmail.com",
                 course="Data Science", marks=35, attendance=60),

    StudentModel(id=6, name="Sneha M", email="sneha@gmail.com",
                 course="Python", marks=96, attendance=98),

    StudentModel(id=7, name="Rakesh V", email="rakesh@gmail.com",
                 course="Web Development", marks=67, attendance=82),

    StudentModel(id=8, name="Pooja N", email="pooja@gmail.com",
                 course="Cloud Computing", marks=55, attendance=75)
]


# Helper Function: Search Students
def search_students(data, keyword):
    if not keyword:
        return data

    keyword = keyword.lower()

    return [
        student for student in data
        if keyword in student.name.lower()
        or keyword in student.email.lower()
    ]


# Helper Function: Filter by Course
def filter_by_course(data, course_name):
    if not course_name:
        return data

    return [
        student for student in data
        if student.course.lower() == course_name.lower()
    ]


# Helper Function: Filter by Marks
def filter_by_marks(data, minimum, maximum):
    if minimum is not None:
        data = [student for student in data
                if student.marks >= minimum]

    if maximum is not None:
        data = [student for student in data
                if student.marks <= maximum]

    return data


# Helper Function: Filter Pass / Fail
def filter_by_result(data, passed):
    if passed is None:
        return data

    if passed:
        return [student for student in data if student.marks >= 50]

    return [student for student in data if student.marks < 50]


# Helper Function: Calculate Grade
def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# Root Endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to Student Performance API",
        "documentation": "/docs",
        "available_routes": [
            "/students",
            "/students/{student_id}",
            "/students/{student_id}/result",
            "/courses",
            "/analytics"
        ]
    }


# Get All Students with Filters
@app.get("/students", response_model=List[StudentModel])
def get_all_students(
    search: Optional[str] = None,
    course: Optional[str] = None,
    min_marks: Optional[float] = Query(None, ge=0, le=100),
    max_marks: Optional[float] = Query(None, ge=0, le=100),
    passed: Optional[bool] = None,
    sort_by: str = Query("id", pattern="^(id|name|marks|attendance)$"),
    order: str = Query("asc", pattern="^(asc|desc)$"),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):

    result = students.copy()

    result = search_students(result, search)
    result = filter_by_course(result, course)
    result = filter_by_marks(result, min_marks, max_marks)
    result = filter_by_result(result, passed)

    result.sort(
        key=lambda student: getattr(student, sort_by),
        reverse=(order == "desc")
    )

    return result[offset:offset + limit]


# Get Student by ID
@app.get("/students/{student_id}", response_model=StudentModel)
def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Get Student Result
@app.get("/students/{student_id}/result")
def get_student_result(student_id: int):

    for student in students:
        if student.id == student_id:

            grade = get_grade(student.marks)

            return {
                "student_id": student.id,
                "student_name": student.name,
                "course": student.course,
                "marks": student.marks,
                "grade": grade,
                "attendance": student.attendance,
                "result": "Pass" if student.marks >= 50 else "Fail"
            }

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Get Course Details
@app.get("/courses")
def get_courses():

    course_details = {}

    for student in students:
        course = student.course

        if course not in course_details:
            course_details[course] = 0

        course_details[course] += 1

    return [
        {
            "course_name": course,
            "total_students": count
        }
        for course, count in course_details.items()
    ]


# Get Class Analytics
@app.get("/analytics")
def get_analytics():

    total_students = len(students)

    if total_students == 0:
        return {"message": "No student records available"}

    total_marks = sum(student.marks for student in students)

    passed_students = [
        student for student in students
        if student.marks >= 50
    ]

    highest = max(students, key=lambda student: student.marks)
    lowest = min(students, key=lambda student: student.marks)

    return {
        "total_students": total_students,
        "average_marks": round(total_marks / total_students, 2),
        "passed_students": len(passed_students),
        "failed_students": total_students - len(passed_students),
        "highest_scorer": highest.name,
        "highest_marks": highest.marks,
        "lowest_scorer": lowest.name,
        "lowest_marks": lowest.marks
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
