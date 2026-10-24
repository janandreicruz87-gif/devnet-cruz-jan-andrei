import requests

pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-form/1/')
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-form/4/')
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-form/7/')
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-form/19/')
pokemon = requests.get('https://pokeapi.co/api/v2/pokemon-form/13/')

random.choice
print(random.choice(bulbasaur, charmander, squirtle, rattata, weedle))