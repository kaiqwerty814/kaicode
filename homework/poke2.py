import requests

data = "https://pokeapi.co/api/v2/pokemon/squirtle"

response = requests.get(data)

mutant_data = response.json

print(mutant_data["name"])

print(mutant_data["base_expirience"])

print(mutant_data[""])