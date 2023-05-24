import json
import re

def parse_json(nombre_archivo):
    lista_jugadores = []
    
    with open(nombre_archivo, "r") as archivo:
        data = json.load(archivo)
        lista_jugadores = data["jugadores"]

    return lista_jugadores

lista_jugadores = parse_json(r"C:\Users\Usuario\Desktop\python\parcial\dt.json")


def obtener_nombre(dic_jugadores):
    mensaje = "{0} - {1}".format(dic_jugadores["nombre"],dic_jugadores["posicion"])
    return mensaje
 

def imprimir_dato(string):
    print(string)


def mostrar_lista_de_jugadores(lista_jugadores):
    for jugador in lista_jugadores:
                nombre = obtener_nombre(jugador)
                imprimir_dato(nombre)
    
    