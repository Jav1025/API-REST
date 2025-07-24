import requests

URL = "https://pokeapi.co/api/v2/pokemon"

respuesta = requests.get(URL)
datos = respuesta.json()
print(datos)



