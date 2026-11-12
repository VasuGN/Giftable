
# Personal Expense Tracker

## Project Description

A beginner-friendly Personal Expense Tracker built using Python, FastAPI, HTML, CSS, and JavaScript.

Users can add, view, update, and delete their personal expenses.

All expense records are stored in a JSON file so that data persists even after restarting the application.

## Technologies Used

- Python
- FastAPI
- Pydantic
- HTML
- CSS
- JavaScript
- JSON File Storage

## Project Structure

Personal_Expense_Tracker/
│
├── main.py
├── index.html
├── README.md
└── expenses.json (automatically generated)

## Installation

### 1. Create virtual environment

python -m venv venv

### 2. Activate virtual environment

Windows:

venv\Scripts\activate

### 3. Install dependencies

pip install fastapi uvicorn

### 4. Run application

uvicorn main:app --reload

### 5. Open application

http://127.0.0.1:8000/

### 6. Open API documentation

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /expenses | Add expense |
| GET | /expenses | View all expenses |
| PUT | /expenses/{expense_id} | Update expense |
| DELETE | /expenses/{expense_id} | Delete expense |

## Data Storage

All expense records are stored in expenses.json.

The application loads existing records when it starts and saves changes whenever an expense is added, updated, or deleted.

## Features

1. Add a new expense.
2. View all expenses.
3. Update existing expenses.
4. Delete expenses.
5. Calculate total expenses.
6. Persistent JSON file storage.
7. Input validation using Pydantic.

## Author

Personal Expense Tracker - Weekly Assignment
