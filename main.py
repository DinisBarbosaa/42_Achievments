from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() #creates a object that will hold all the routes

# 2. Define what a "Student" looks like using Pydantic
class StudentCreate(BaseModel):
    name: str
    age: int
    grade: float
    is_active: bool = True 

	
@app.get("/")  #whenever someone makes a GET request, it runs the function bellow
def read_root():
	return {"message" : "Hello from 42 Achievements!"}

# {student_id} is a path parameter — required, identifies a specific resource.
@app.get("/student/{student_id}")  
def read_student(student_id: int):
    return {"student_id" : student_id}

# "name" is a query parameter (comes after "?" in the URL).
@app.get("/search")
def search_students(name: str):
    return {"searching_for_name": name}

@app.post("/students") #We use .post instead of .get
def create_student(student: StudentCreate):
    return {
        "message": "Student created successfully!",
        "received_data": student # FastAPI converts this Pydantic model back to JSON for the response
    }


#http://localhost:8000/docs