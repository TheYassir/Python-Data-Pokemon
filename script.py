import json
import requests

# Generation 1
api_url = "https://pokeapi.co/api/v2/pokemon?limit=151"
# Generation 2
# api_url = "https://pokeapi.co/api/v2/pokemon?offset=151&limit=100"
# Generation 1-2
# api_url = "https://pokeapi.co/api/v2/pokemon?limit=251"

response = requests.get(api_url)
data = response.json()
pokemons = []

for pokemon in data['results']:
  req = requests.get(pokemon['url'])
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

f = open(f'data/data.json', mode="w")
f.write(json.dumps(pokemons))