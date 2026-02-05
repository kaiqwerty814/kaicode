
#1. imprted requests because it has a function to help us get the api data
import requests

#2.Make a variable that equals the link(url) to store the link(url)
api_link = "https://pokeapi.co/api/v2/pokemon/pikachu"

#3.make another variable to save what our butler(requests) has gotten from the link(url)
resonse = requests.get(api_link)

#4.we get the content of resonse and get the json function
jsondata = resonse.json()
# content.getTheInfoPart()

#ASSINGMENT: print out the name, id and height

#Name
print()

#Id
print()

#Height
print()