import json
import time

latitudeList = []
longitudeList = []
allLocations = []

def add_location(Latitude: float, Longitude: float, ID: int):
    location = {
        "id": ID,
        "lat": Latitude,
        "long": Longitude
    }
    allLocations.append(location)

add_location(51.408094, 5.417924, 3)
add_location(51.423617, 5.404349, 3)
add_location(51.433143, 5.419466, 3)
add_location(51.443523, 5.443262, 3)
add_location(51.444379, 5.464047, 3)
add_location(51.435283, 5.471433, 3)
add_location(51.428809, 5.461088, 3)
add_location(51.419068, 5.445284, 3)
add_location(51.408308, 5.429137, 3)
add_location(51.438440, 5.418144, 3)

print(allLocations)