# Eigen inbreng project
# Een script die ervoor zorgt dat de locatie van verschillende agenten om de x secondes wordt upgedate.
# Er moet een lijst zijn met verschillende waardes met LAT & LONG voor elk agent. (List)

import requests
import json
import time
import threading

# latitudeList = []
# longitudeList = []
# allLocations = [{'id': 1, 'lat': 51.463526, 'long': 5.474311}, {'id': 1, 'lat': 51.460959, 'long': 5.469501}, {'id': 1, 'lat': 51.456895, 'long': 5.470017}, {'id': 1, 'lat': 51.453526, 'long': 5.467256}, {'id': 1, 'lat': 51.4493, 'long': 5.470176}, {'id': 1, 'lat': 51.446197, 'long': 5.473955}, {'id': 1, 'lat': 51.447214, 'long': 5.47971}, {'id': 1, 'lat': 51.447802, 'long': 5.487869}, {'id': 1, 'lat': 51.44946, 'long': 5.498347}, {'id': 1, 'lat': 51.451814, 'long': 5.479655}]
agent1 = [{'id': 1, 'lat': 51.463526, 'long': 5.474311}, {'id': 1, 'lat': 51.460959, 'long': 5.469501}, {'id': 1, 'lat': 51.456895, 'long': 5.470017}, {'id': 1, 'lat': 51.453526, 'long': 5.467256}, {'id': 1, 'lat': 51.4493, 'long': 5.470176}, {'id': 1, 'lat': 51.446197, 'long': 5.473955}, {'id': 1, 'lat': 51.447214, 'long': 5.47971}, {'id': 1, 'lat': 51.447802, 'long': 5.487869}, {'id': 1, 'lat': 51.44946, 'long': 5.498347}, {'id': 1, 'lat': 51.451814, 'long': 5.479655}]
agent2 = [{'id': 2, 'lat': 51.463526, 'long': 5.474311}, {'id': 2, 'lat': 51.460959, 'long': 5.469501}, {'id': 2, 'lat': 51.456895, 'long': 5.470017}, {'id': 2, 'lat': 51.453526, 'long': 5.467256}, {'id': 2, 'lat': 51.4493, 'long': 5.470176}, {'id': 2, 'lat': 51.446197, 'long': 5.473955}, {'id': 2, 'lat': 51.447214, 'long': 5.47971}, {'id': 2, 'lat': 51.447802, 'long': 5.487869}, {'id': 2, 'lat': 51.44946, 'long': 5.498347}, {'id': 2, 'lat': 51.451814, 'long': 5.479655}]
agent3 = [{'id': 3, 'lat': 51.463526, 'long': 5.474311}, {'id': 3, 'lat': 51.460959, 'long': 5.469501}, {'id': 3, 'lat': 51.456895, 'long': 5.470017}, {'id': 3, 'lat': 51.453526, 'long': 5.467256}, {'id': 3, 'lat': 51.4493, 'long': 5.470176}, {'id': 3, 'lat': 51.446197, 'long': 5.473955}, {'id': 3, 'lat': 51.447214, 'long': 5.47971}, {'id': 3, 'lat': 51.447802, 'long': 5.487869}, {'id': 3, 'lat': 51.44946, 'long': 5.498347}, {'id': 3, 'lat': 51.451814, 'long': 5.479655}]
agents = [agent1, agent2, agent3]
threads = []

# def add_location(Latitude: float, Longitude: float, ID: int):
#     location = {
#         "id": ID,
#         "lat": Latitude,
#         "long": Longitude
#     }
#     allLocations.append(location)

# add_location(51.463526, 5.474311, 1)
# add_location(51.460959, 5.469501, 1)
# add_location(51.456895, 5.470017, 1)
# add_location(51.453526, 5.467256, 1)
# add_location(51.449300, 5.470176, 1)
# add_location(51.446197, 5.473955, 1)
# add_location(51.447214, 5.479710, 1)
# add_location(51.447802, 5.487869, 1)
# add_location(51.449460, 5.498347, 1)
# add_location(51.451814, 5.479655, 1)

# print(allLocations)

def move_Agent(locations):
    for location in locations:
        json_object = json.dumps(location, indent = 4)
        r = requests.post("https://api.blue-trace.nl/update-agent-location/", data=json_object)
        print(f'Request was {r.status_code}')
        time.sleep(10)

while True:

    for agent in agents:
        t = threading.Thread(target=move_Agent, args=[agent])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()