import requests
import random
import json

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(id):
    url = f"{base_url}/pokemon/{id}"
    response = requests.get(url)

# check if response received
    if response.status_code == 200:
        pokemon_data = response.json()
        return(pokemon_data)
    else:
        print("Failed to retrieve data")

# input for number of pokemon
# loops until the input is an integer
poke_num = ""
while True:
    poke_num = input("How many random pokemon would you like to view? --> ")
    try:
        poke_num = int(poke_num)
        break
    except ValueError:
        continue

pokemon_list = []

# loops for number of pokemon input
for x in range(poke_num):
#   range of valid pokemon
    poke_id = random.randint(1, 1025)
    pokemon_info = get_pokemon_info(poke_id)

#   pull each pokemon information
    if pokemon_info:
        name = pokemon_info["name"].capitalize()
        poke_id = pokemon_info["id"]
        poke_type = pokemon_info["types"][0]["type"]["name"].capitalize() if pokemon_info["types"] else "Unknown"

#       add each pokemon to list
        pokemon_list.append({
            "name": name,
            "id": poke_id,
            "type": poke_type
        })

        print(f"Name: {name}, ID: {poke_id}, Type: {poke_type}")

# create and insert into json file
with open("pokemon_data.json", "w") as json_file:
    json.dump(pokemon_list, json_file, indent=4)

print("File created")
