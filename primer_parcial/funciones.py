
import json
import re
import csv

def parse_json(nombre_archivo):
    lista_jugadores = []
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
        lista_jugadores = data["jugadores"]

    return lista_jugadores

ruta = r"C:\Users\Usuario\Desktop\primer_parcial\primer_parcial\dt.json"
lista_jugadores = parse_json(ruta)


def obtener_nombre(dic_jugadores):
    mensaje = "{0} - {1}".format(dic_jugadores["nombre"],dic_jugadores["posicion"])
    return mensaje
 

def obtener_estadisticas(dic_jugadores):
    estadisticas = dic_jugadores["estadisticas"]
    mensaje = "temporadas jugadas: {0}\npuntos totales: {1}\npromedio de puntos por partido: {2}\nrebotes totales: {3}\npromedio de rebotes por partido: {4}\nasistencias totales: {5}\npromedio de asistencias por partido: {6}\nrobos totales: {7}\nbloqueos totales: {8}\nporcentaje de tiros de campo: {9}\nporcentaje de tiros libres: {10}\nporcentaje de tiros triples: {11}".format(estadisticas["temporadas"], estadisticas["puntos_totales"], estadisticas["promedio_puntos_por_partido"], estadisticas["rebotes_totales"], estadisticas["promedio_rebotes_por_partido"], estadisticas["asistencias_totales"], estadisticas["promedio_asistencias_por_partido"], estadisticas["robos_totales"], estadisticas["bloqueos_totales"], estadisticas["porcentaje_tiros_de_campo"], estadisticas["porcentaje_tiros_libres"], estadisticas["porcentaje_tiros_triples"])
    return mensaje

def obtener_logros(dic_jugadores):
    logros = dic_jugadores["logros"]
    mensaje = "{0}".format(dic_jugadores["logros"])
    return mensaje


def imprimir_dato(string):
    print(string)


def mostrar_lista_de_jugadores(lista_jugadores):
    for jugador in lista_jugadores:
                nombre = obtener_nombre(jugador)
                imprimir_dato(nombre)
 
def buscar_jugador(lista_jugadores, seleccion):
    seleccion = int(seleccion)

    if seleccion >= 0 and seleccion < len(lista_jugadores):
        jugador = lista_jugadores[seleccion]
        nombre = obtener_nombre(jugador)
        imprimir_dato(nombre)
        estadisticas = obtener_estadisticas(jugador)
        imprimir_dato(estadisticas)
    else: 
        print("El jugador no fue encontrado")

def guardar_en_csv(ruta, jugador):
    # Obtener el nombre y las estadísticas formateadas del jugador
    nombre = obtener_nombre(jugador)
    estadisticas = obtener_estadisticas(jugador)

    # Formatear los datos en el formato deseado
    datos_formateados = "{0}\n\n{1}".format(nombre, estadisticas)

    # Guardar los datos en un archivo CSV
    with open(ruta, 'w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(["Datos del Jugador"])
        escritor_csv.writerow([datos_formateados])

def buscar_jugador_por_nombre(lista_jugadores, nombre_jugador):
    jugadores_coincidentes = []

    for jugador in lista_jugadores:
        if nombre_jugador.lower() in jugador["nombre"].lower():
            jugadores_coincidentes.append(jugador)

    if jugadores_coincidentes:
        print("Jugadores coincidentes:")
        for jugador in jugadores_coincidentes:
            nombre = obtener_nombre(jugador)
            imprimir_dato(nombre)
            logros = obtener_logros(jugador)
            imprimir_dato(logros)
    else:
        print("No se encontraron jugadores coincidentes")


def calcular_promedio_puntos_equipo(lista_jugadores):
    
    puntos_por_jugador = []

    # Calcular puntos por partido para cada jugador
    for jugador in lista_jugadores:
        puntos_totales = jugador["estadisticas"]["puntos_totales"]
        temporadas = jugador["estadisticas"]["temporadas"]
        puntos_por_partido = puntos_totales / temporadas
        puntos_por_jugador.append((jugador["nombre"], puntos_por_partido))

    # Ordenar jugadores por nombre de manera ascendente (lógica de ordenamiento manual)
    n = len(puntos_por_jugador)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if puntos_por_jugador[j][0] > puntos_por_jugador[j + 1][0]:
                puntos_por_jugador[j], puntos_por_jugador[j + 1] = puntos_por_jugador[j + 1], puntos_por_jugador[j]

    # Mostrar promedio de puntos por partido para todo el equipo
    print("Promedio de puntos por partido del equipo del Dream Team:")
    for jugador in puntos_por_jugador:
        print("- {0}: {1}".format(jugador[0], jugador[1]))


def verificar_miembro_hall_of_fame(lista_jugadores,nombre_jugador):
    
    for jugador in lista_jugadores:
        if jugador["nombre"].lower() == nombre_jugador.lower():
            if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                print("{0} es miembro del Salón de la Fama del Baloncesto.".format(nombre_jugador))
            else:
                print("{0} no es miembro del Salón de la Fama del Baloncesto.".format(nombre_jugador))
            return

    print("No se encontró información del jugador {0}.".format(nombre_jugador))






