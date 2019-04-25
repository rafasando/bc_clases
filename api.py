'''
import requests
from pprint import pprint
API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "The Matrix"

busqueda = URL + API_KEY + "&t=" + titulo

respuesta = requests.get(busqueda)
dic_peli = respuesta.json()

pprint(dic_peli)

# Ejercicio
# Consultar el API de OMDB 
# y obtener el nombre del Director de Fight Club

import requests
from pprint import pprint

API_KEY = "595695c3"
URL = "http://www.omdbapi.com/?apikey="
titulo = "Fight Club"

busqueda = URL + API_KEY + "&t=" + titulo
respuesta = requests.get(busqueda)
dic_peli = respuesta.json()

print(dic_peli["Director"])
'''


# Ejercicio
# Crear una funcion
# que reciba como argumento el titulo de una pelicula 
# y retorne los actores de esa pelicula

import requests
from pprint import pprint


def actores_de_peli(arg_titulo):
    API_KEY = "595695c3"
    URL = "http://www.omdbapi.com/?apikey="
    busqueda = URL + API_KEY + "&t=" + arg_titulo
    pelicula = requests.get(busqueda).json()
    return pelicula["Actors"]

nombre_peli = input("Escriba el nombre de la peli:")
print("")
print("Los actores de la", nombre_peli, "son:")
pprint(actores_de_peli(nombre_peli))
