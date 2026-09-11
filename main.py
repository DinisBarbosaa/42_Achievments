from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import engine, get_db, Base
from models import Student

# Creates the actual tables in Postgres based on your models.
# Only creates what doesn't already exist — safe to run every startup.
Base.metadata.create_all(bind=engine)

app = FastAPI()  # creates an object that will hold all the routes


# Define what a "Student" request looks like using Pydantic
class StudentCreate(BaseModel):
    name: str
    age: int
    grade: float
    is_active: bool = True


@app.get("/")  # whenever someone makes a GET request, it runs the function below
def read_root():
    return {"message": "Hello from 42 Achievements!"}


# {student_id} is a path parameter — required, identifies a specific resource.
@app.get("/student/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.id == student_id).first()


# "name" is a query parameter (comes after "?" in the URL).
@app.get("/search")
def search_students(name: str, db: Session = Depends(get_db)):
    return db.query(Student).filter(Student.name == name).all()


@app.post("/students")  # We use .post instead of .get
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(
        name=student.name,
        age=student.age,
        grade=student.grade,
        is_active=student.is_active,
    )
    db.add(new_student)       # stage the new row
    db.commit()                # actually write it to Postgres
    db.refresh(new_student)    # pull back the auto-generated id
    return new_student


@app.get("/students")
def list_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


#http://localhost:8000/docs