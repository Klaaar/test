import requests
import json

url = 'https://swapi.dev/api/'

response = requests.get(url).json()
people_api = response.get('people')
planets_api = response.get('planets')
starships_api = response.get('starships')

def check_people(url):
    for i in range(1,6):
        response = requests.get(f'{url}/{i}').json()
        print(response)

def check_pl(url):
    diam = []
    for i in range(1, 6):
        response = requests.get(f'{url}/{i}').json()
        diam.append({response.get('name'): response.get('diameter')})
        print(diam)
#--------------------------------------------------------
def check_st_sh(url):
    for i in range(1,6):
        sp = []
        response = requests.get(f'{url}/{i}').json()
        sp.append(response.get('max_atmosphering_speed'))
        print(sp)

check_st_sh(starships_api)