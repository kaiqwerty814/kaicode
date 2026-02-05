import requests
import random

pikachu_data = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print(pikachu_data.json()["name"])

