import csv
import json


class Student:
    def __init__(self, name, subject, marks):
        self.name = name
        self.subject = subject
        self.__marks = 0
        self.set_marks(marks)

    def set_marks(self, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def __str__(self):
        return f"{self.name} | {self.subject} | {self.__marks}"


students = [
    Student("Vasu", "Python", 85),
    Student("Rahul", "Javascript", 72),
    Student("Pramod", "Java", 91),
    Student("Sagar", "Python", 68),
    Student("Puneeth", "Java", 78),
]

for student in students:
    print(student)

# Convert objects into dictionaries
records = [
    {
        "name": s.name,
        "subject": s.subject,
        "marks": s.get_marks()
    }
    for s in students
]

# Write TXT file
with open("students.txt", "w", encoding="utf-8") as f:
    for row in records:
        f.write(
            f"{row['name']},{row['subject']},{row['marks']}\n"
        )


# Write CSV file
with open("students.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["name", "subject", "marks"]
    )
    writer.writeheader()
    writer.writerows(records)


# Write JSON file
with open("students.json", "w", encoding="utf-8") as f:
    json.dump(records, f, indent=2)


# Read files
for filename in ["students.txt", "students.csv", "students.json"]:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print(f"\n--- {filename} ---")
            print(f.read())

    except FileNotFoundError:
        print("File not found:", filename)

    except ValueError:
        print("Invalid value in:", filename)

    finally:
        print("File operation finished.")
