from fastapi import FastAPI
app = FastAPI() #create a FastAPI instance

#GET PUT POST DELETE PATCH

@app.get("/") #decorator to define a GET endpoint
def home():
    return {"message": "Hello, World!"} #return a JSON response

@app.get("/login")
def login():
    return {"message": "Login successful"} 

@app.get("/register")
def register():
    username = "JohnDoe"
    password = "password123"
    return {"my details": f"Username: {username}, Password: {password}"}