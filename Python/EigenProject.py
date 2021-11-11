# Eigen inbreng project
# Een script die ervoor zorgt dat de locatie van verschillende agenten om de x secondes wordt upgedate.
# Er moet een lijst zijn met verschillende waardes met LAT & LONG voor elk agent. (List)

import requests

latitudeList = []
longitudeList = []
allLocations = []

def add_location(Latitude, Longitude):
    location = {
        "lat": Latitude,
        "long": Longitude,
    }
    allLocations.append(location)

add_location(51.463526, 5.474311)
add_location(51.460959, 5.469501)
add_location(51.456895, 5.470017)
add_location(51.453526, 5.467256)
add_location(51.449300, 5.470176)
add_location(51.446197, 5.473955)
add_location(51.447214, 5.479710)
add_location(51.447802, 5.487869)
add_location(51.449460, 5.498347)
add_location(51.451814, 5.479655)

for locations in allLocations:
    print(locations)
    r = requests.post("", params=allLocations[locations])