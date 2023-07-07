import json
import requests

# choose your pokemon_id and set is id here
# id 6 for Charizard = Dracaufeu
CHOOSE_POKEMON = 6 


pokemons = []

req = requests.get(f'https://pokeapi.co/api/v2/pokemon/{CHOOSE_POKEMON}')
datareq = req.json()

reqspecie = requests.get(datareq['species']['url'])
datareqspecie = reqspecie.json()

reqevol = requests.get(datareqspecie['evolution_chain']['url'])
dataevol = reqevol.json()

poke = {
  "id": datareq['id'],
  "name": datareq['name'],
  "weight": datareq['weight'],
  "height": datareq['height'],
  "img": datareq['sprites']['front_default'],
  "imgshiny": datareq['sprites']['front_shiny'],
  "types": datareq['types'],
  "stats": datareq['stats'],
  "species": {
    "base_happiness": datareqspecie['base_happiness'],
    "capture_rate": datareqspecie['capture_rate'],
    "is_legendary": datareqspecie['is_legendary'],
    "is_mythical": datareqspecie['is_mythical'], 
    "color": datareqspecie['color']["name"]
  },
  "evolution": dataevol['chain'],
}
pokemons.append(poke)

f = open(f'data/onedata.json', mode="w")
f.write(json.dumps(pokemons))