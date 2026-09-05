from fastapi import FastAPI

app = FastAPI() #creates a object that will hold all the routes

@app.get("/")  #whenever someone makes a GET request, it runs the function bellow"
def read_root():
	return {"message" : "Hello from 42 Achievements!"}