from fastapi import FastAPI

app = FastAPI()  # create a FastAPI instance

# GET PUT POST DELETE PATCH


@app.get("/")  # decorator to define a GET endpoint
def home():
    return {"message": "Welcome to Hotel Room Booking"}  # return a JSON response


@app.get("/rooms")
def rooms():
    return {"message": "Rooms available: Single, Double, Suite"}


@app.get("/book")
def book():
    room_type = "Double"
    guest_name = "JohnDoe"
    return {"booking_details": f"Guest: {guest_name}, Room: {room_type}, Status: Confirmed"}


@app.get("/checkin")
def checkin():
    return {"message": "Check-in successful"}


@app.get("/checkout")
def checkout():
    return {"message": "Checkout successful"}


@app.get("/contact")
def contact():
    phone = "123-456-7890"
    email = "hotel@example.com"
    return {"contact_details": f"Phone: {phone}, Email: {email}"}
