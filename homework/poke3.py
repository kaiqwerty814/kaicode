import requests

rna = "https://pokeapi.co/api/v2/pokemon/gengar"

response = requests.get(rna)

dna = response.json()

print(dna["name"])

print(dna["base_experience"])

print(dna["game_indices"])