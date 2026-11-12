
from pathlib import Path
import json

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field


app = FastAPI(title="Personal Expense Tracker")

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "expenses.json"

expenses = []
next_id = 1


# Pydantic model
class Expense(BaseModel):
    title: str
    amount: float = Field(gt=0)
    category: str
    date: str


# Load expenses from JSON file
def load_expenses():
    global expenses, next_id

    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as file:
            expenses = json.load(file)
    else:
        expenses = []

    if expenses:
        next_id = max(expense["id"] for expense in expenses) + 1
    else:
        next_id = 1


# Save expenses to JSON file
def save_expenses():
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


# Load existing data when application starts
load_expenses()


# Home page
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


# READ - Get all expenses
@app.get("/expenses")
def get_expenses():
    return expenses


# CREATE - Add a new expense
@app.post("/expenses")
def add_expense(expense: Expense):
    global next_id

    new_expense = {
        "id": next_id,
        **expense.model_dump()
    }

    expenses.append(new_expense)
    save_expenses()

    next_id += 1

    return new_expense


# UPDATE - Update an existing expense
@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, expense: Expense):

    for index, current_expense in enumerate(expenses):

        if current_expense["id"] == expense_id:

            expenses[index] = {
                "id": expense_id,
                **expense.model_dump()
            }

            save_expenses()

            return expenses[index]

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )


# DELETE - Delete an expense
@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    for index, expense in enumerate(expenses):

        if expense["id"] == expense_id:

            deleted_expense = expenses.pop(index)

            save_expenses()

            return {
                "message": "Expense deleted successfully",
                "deleted_expense": deleted_expense
            }

    raise HTTPException(
        status_code=404,
        detail="Expense not found"
    )
