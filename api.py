from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List, Dict
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware to allow connections from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Location(BaseModel):
    latitude: float
    longitude: float

class User(BaseModel):
    name: str
    gender: str
    blood_group: str
    bluetoothName: str
    wifiName: str
    location: Location

# Storage for user streams
active_data: List[User] = []

active_data.append(User(
    name="John Doe",
    gender="Male",
    blood_group="O+",
    bluetoothName="John's Bluetooth",
    wifiName="John's WiFi",
    location=Location(latitude=37.7749, longitude=-122.4194)
))

active_data.append(User(
    name="Jane Doe",
    gender="Female",
    blood_group="A+",
    bluetoothName="Jane's Bluetooth",
    wifiName="Jane's WiFi",
    location=Location(latitude=40.7128, longitude=-74.0060)
))


# API Endpoints
@app.post("/stream/location")
async def receive_location(user: User):
    """Accepts user location data and adds it to the active_data list."""
    # Update or add user location
    for existing_user in active_data:
        if existing_user.name == user.name:
            existing_user.location = user.location
            break
    else:
        active_data.append(user)

    return JSONResponse(content={"message": "Location updated successfully!"}, status_code=200)

@app.get("/stream/data")
async def get_stream_data():
    """Returns the current active data."""
    return JSONResponse(content=[user.dict() for user in active_data], status_code=200)




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
