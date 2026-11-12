# Student CRUD — Create and Read

An HTML page connected to FastAPI. It can add students and display all students.

## Run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```
Open http://127.0.0.1:8000. API documentation: http://127.0.0.1:8000/docs

## Features
- Create a student with name, age and course.
- Read/list all students.
- Data is stored in memory and resets when the server restarts.
