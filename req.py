from modals import User, Location

import requests

location = Location(
    latitude=12.9716,
    longitude=77.5946
)



user_data = {
    "id": 1,
    "name": "Praful M",
    "gender": "Male",
    "blood_group": "O+",
    "bluetoothName": "Praful's Bluetooth",
    "wifiName": "Praful's WiFi",
    "location": {
        "latitude": location.latitude,
        "longitude": location.longitude
    }
}




response = requests.post('http://0.0.0.0:8000/v1/api/distress', json=user_data)
print(response)