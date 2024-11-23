from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float

class User(BaseModel):
    name: str
    gender: str
    blood_group: str
    bluetoothName: str
    wifiName: str
    location : Location

