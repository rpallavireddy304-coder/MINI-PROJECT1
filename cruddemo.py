from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Temporary database
students = []

# Student model
class Student(BaseModel):
    id: int
    name: str
    age: int
    course: str


# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Student Management API"}


# Add student
@app.post("/students")
def add_student(student: Student):
    students.append(student)
    return {
        "message": "Student added successfully",
        "student": student
    }


# Get all students
@app.get("/students")
def get_students():
    return students


# Get student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )


# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return {"message": "Student updated successfully"}

    raise HTTPException(status_code=404, detail="Student not found")


# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student.id == student_id:
            students.remove(student)
            return {"message": "Student deleted successfully"}

    raise HTTPException(status_code=404, detail="Student not found")