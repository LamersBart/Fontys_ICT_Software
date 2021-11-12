import requests
import json
import time
import threading

agent1 = [{'id': 1, 'lat': 51.466628, 'long': 5.469398}, {'id': 1, 'lat': 51.464007, 'long': 5.459702}, {'id': 1, 'lat': 51.47144, 'long': 5.45326}, {'id': 1, 'lat': 51.481917, 'long': 5.449567}, {'id': 1, 'lat': 51.490736, 'long': 5.4518}, {'id': 1, 'lat': 51.496133, 'long': 5.466058}, {'id': 1, 'lat': 51.485071, 'long': 5.489505}, {'id': 1, 'lat': 51.475556, 'long': 5.488474}, {'id': 1, 'lat': 51.467643, 'long': 5.4871}, {'id': 1, 'lat': 51.467216, 'long': 5.474561}]
agent2 = [{'id': 2, 'lat': 51.441169, 'long': 5.4727}, {'id': 2, 'lat': 51.444272, 'long': 5.50283}, {'id': 2, 'lat': 51.439082, 'long': 5.513782}, {'id': 2, 'lat': 51.432287, 'long': 5.502978}, {'id': 2, 'lat': 51.425437, 'long': 5.507769}, {'id': 2, 'lat': 51.416766, 'long': 5.503317}, {'id': 2, 'lat': 51.416445, 'long': 5.483563}, {'id': 2, 'lat': 51.428648, 'long': 5.486827}, {'id': 2, 'lat': 51.435176, 'long': 5.471367}, {'id': 2, 'lat': 51.43844, 'long': 5.471661}]
agent3 = [{'id': 3, 'lat': 51.408094, 'long': 5.417924}, {'id': 3, 'lat': 51.423617, 'long': 5.404349}, {'id': 3, 'lat': 51.433143, 'long': 5.419466}, {'id': 3, 'lat': 51.443523, 'long': 5.443262}, {'id': 3, 'lat': 51.444379, 'long': 5.464047}, {'id': 3, 'lat': 51.435283, 'long': 5.471433}, {'id': 3, 'lat': 51.428809, 'long': 5.461088}, {'id': 3, 'lat': 51.419068, 'long': 5.445284}, {'id': 3, 'lat': 51.408308, 'long': 5.429137}, {'id': 3, 'lat': 51.43844, 'long': 5.418144}]
agents = [agent1, agent2, agent3]
threads = []

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