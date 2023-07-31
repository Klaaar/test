import requests

response = requests.get('https://swapi.dev/api/starships/').json()
starships_api = response.get('results')

max_speed = 0
fastest_ship = ""

for ship in starships_api:
    speed = ship.get("max_atmosphering_speed")
    if speed == "unknown":
        continue
    speed = int(speed)
    if speed > max_speed:
        max_speed = speed
        fastest_ship = ship.get("name")

print("The fastest ship is:", fastest_ship)