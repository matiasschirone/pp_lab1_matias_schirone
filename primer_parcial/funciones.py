
import json
import re
import csv

def parse_json(nombre_archivo):
    """
    Esta función lee un archivo JSON y devuelve una lista de jugadores.
    
    :param nombre_archivo: El parámetro "nombre_archivo" es una cadena que representa el nombre del
    archivo JSON que contiene los datos a analizar
    :return: una lista de jugadores (lista_jugadores) analizada a partir de un archivo JSON especificado
    por el parámetro de entrada (nombre_archivo).
    """
    lista_jugadores = []
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
        lista_jugadores = data["jugadores"]

    return lista_jugadores

ruta = r"C:\Users\Usuario\Desktop\primer_parcial\primer_parcial\dt.json"
lista_jugadores = parse_json(ruta)


def obtener_nombre(dic_jugadores):
    """
    La función "obtener_nombre" devuelve un mensaje de cadena que contiene el nombre y la posición del
    jugador de un diccionario de jugadores.
    
    :param dic_jugadores: Un diccionario que contiene información sobre un jugador, incluido su nombre y
    posición
    :return: una cadena que concatena el nombre y la posición del jugador de un diccionario de
    jugadores.
    """
    mensaje = "{0} - {1}".format(dic_jugadores["nombre"],dic_jugadores["posicion"])
    return mensaje
 

def obtener_estadisticas(dic_jugadores):
    """
    La función toma un diccionario de estadísticas de jugadores y devuelve una cadena formateada con
    varias estadísticas.
    
    :param dic_jugadores: Un diccionario que contiene información sobre un jugador de baloncesto,
    incluidas sus estadísticas
    :return: una cadena formateada con estadísticas de un jugador de baloncesto, obtenida de un
    diccionario que contiene las estadísticas del jugador.
    """
    estadisticas = dic_jugadores["estadisticas"]
    mensaje = "temporadas jugadas: {0}\npuntos totales: {1}\npromedio de puntos por partido: {2}\nrebotes totales: {3}\npromedio de rebotes por partido: {4}\nasistencias totales: {5}\npromedio de asistencias por partido: {6}\nrobos totales: {7}\nbloqueos totales: {8}\nporcentaje de tiros de campo: {9}\nporcentaje de tiros libres: {10}\nporcentaje de tiros triples: {11}".format(estadisticas["temporadas"], estadisticas["puntos_totales"], estadisticas["promedio_puntos_por_partido"], estadisticas["rebotes_totales"], estadisticas["promedio_rebotes_por_partido"], estadisticas["asistencias_totales"], estadisticas["promedio_asistencias_por_partido"], estadisticas["robos_totales"], estadisticas["bloqueos_totales"], estadisticas["porcentaje_tiros_de_campo"], estadisticas["porcentaje_tiros_libres"], estadisticas["porcentaje_tiros_triples"])
    return mensaje

def obtener_logros(dic_jugadores):
    """
    La función "obtener_logros" devuelve un mensaje de cadena que contiene el valor de la clave "logros"
    de un diccionario determinado.
    
    :param dic_jugadores: Un diccionario que contiene información sobre un jugador, incluidos sus logros
    o "logros"
    :return: una cadena que contiene el valor de la clave "logros" en el diccionario de entrada
    "dic_jugadores".
    """
    logros = dic_jugadores["logros"]
    mensaje = "{0}".format(dic_jugadores["logros"])
    return mensaje


def imprimir_dato(string):
    print(string)


def mostrar_lista_de_jugadores(lista_jugadores):
    """
    La función "mostrar_lista_de_jugadores" imprime los nombres de los jugadores en una lista de
    jugadores dada.
    
    :param lista_jugadores: una lista de jugadores, donde cada jugador se representa como un diccionario
    con su información (como nombre, edad, posición, etc.)
    """
    for jugador in lista_jugadores:
                nombre = obtener_nombre(jugador)
                imprimir_dato(nombre)
 
def buscar_jugador(lista_jugadores, seleccion):
    """
    Esta función busca un jugador en una lista de jugadores e imprime su nombre y estadísticas si los
    encuentra.
    
    :param lista_jugadores: una lista de jugadores
    :param seleccion: El índice del reproductor que se buscará en la lista de reproductores
    """
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
    """
    La función guarda el nombre y las estadísticas de un jugador en un archivo CSV.
    
    :param ruta: La ruta donde se guardará el archivo CSV
    :param jugador: El parámetro "jugador" es una variable que representa un objeto de jugador o una
    estructura de datos que contiene información sobre el nombre y las estadísticas de un jugador
    """
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

# La función `buscar_jugador_por_nombre` toma una lista de jugadores y un nombre de jugador como
# entrada, y busca jugadores cuyo nombre contenga el nombre del jugador de entrada. Si se encuentran
# jugadores coincidentes, imprime sus nombres y logros. Si no se encuentran jugadores coincidentes,
# imprime un mensaje que indica que no se encontraron jugadores.
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

    return jugadores_coincidentes


def calcular_promedio_puntos_equipo(lista_jugadores):
    """
    Esta función calcula el promedio de puntos por juego para cada jugador en una lista dada de
    jugadores y muestra los resultados en orden ascendente por nombre de jugador.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (incluyendo el total de puntos y el número de temporadas jugadas)
    """
    
    puntos_por_jugador = []

    # Calcular puntos por partido para cada jugador
    for jugador in lista_jugadores:
        puntos_totales = jugador["estadisticas"]["puntos_totales"]
        temporadas = jugador["estadisticas"]["temporadas"]
        puntos_por_partido = puntos_totales / temporadas
        puntos_por_jugador.append((jugador["nombre"], puntos_por_partido))

    
    # Este código está realizando una clasificación de burbujas en la lista `puntos_por_jugador` en
    # orden ascendente según el nombre del jugador. A la variable `n` se le asigna la longitud de la
    # lista, y luego se usan dos bucles anidados para iterar a través de la lista y comparar elementos
    # adyacentes. Si el nombre del jugador en el índice `j` es mayor que el nombre del jugador en el
    # índice `j+1`, sus posiciones en la lista se intercambian. Este proceso se repite hasta que la
    # lista se ordena en orden ascendente por nombre de jugador.
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
    """
    Esta función comprueba si un jugador de baloncesto determinado es miembro del Salón de la Fama del
    Baloncesto.
    
    :param lista_jugadores: una lista de diccionarios que contienen información sobre jugadores de
    baloncesto, incluido su nombre y logros
    :param nombre_jugador: El nombre del jugador cuyo estado en el Salón de la Fama necesita ser
    verificado
    :return: La función no devuelve nada explícitamente, pero imprime un mensaje que indica si el
    jugador dado es miembro del Salón de la Fama del Baloncesto o no.
    """
    
    for jugador in lista_jugadores:
        if jugador["nombre"].lower() == nombre_jugador.lower():
            if "Miembro del Salon de la Fama del Baloncesto" in jugador["logros"]:
                print("{0} es miembro del Salón de la Fama del Baloncesto.".format(nombre_jugador))
            else:
                print("{0} no es miembro del Salón de la Fama del Baloncesto.".format(nombre_jugador))
            return

    print("No se encontró información del jugador {0}.".format(nombre_jugador).lower())

'''
def jugador_con_mayor_rebotes(lista_jugadores):
    maximo_rebotes = None
    jugador_con_mas_rebotes = None

    for jugador in lista_jugadores:
        rebotes_totales = jugador["estadisticas"]["rebotes_totales"]
        if maximo_rebotes is None or rebotes_totales > maximo_rebotes:
            maximo_rebotes = rebotes_totales
            jugador_con_mas_rebotes = jugador["nombre"]

    if jugador_con_mas_rebotes is not None:
        print("El jugador con la mayor cantidad de rebotes totales es: {0}".format(jugador_con_mas_rebotes))
        print("Rebotes totales: {0}".format(maximo_rebotes))
    else:
        print("No se encontró información de los jugadores.")


def jugador_con_mayor(lista_jugadores, key):
    maximo = None
    jugador_con_mas = None

    for jugador in lista_jugadores:
        totales = jugador["estadisticas"][key]
        if maximo == None or totales > maximo:
            maximo = totales
            jugador_con_mas = jugador["nombre"]

    if jugador_con_mas_rebotes is not None:
        print("El jugador es: {0}".format(jugador_con_mas))
        print("totales: {0}".format(maximo))
    else:
        print("No se encontró información de los jugadores.")

def jugador_con_mayor_porcentaje_tiros_campo(lista_jugadores):
    maximo_porcentaje = None
    jugador_con_mejor_porcentaje = None

    for jugador in lista_jugadores:
        porcentaje_tiros_de_campo = jugador["estadisticas"]["porcentaje_tiros_de_campo"]
        if maximo_porcentaje == None or porcentaje_tiros_de_campo > maximo_porcentaje:
            maximo_porcentaje = porcentaje_tiros_de_campo
            jugador_con_mejor_porcentaje = jugador["nombre"]

    if jugador_con_mejor_porcentaje is not None:
        print("El jugador con mejor porcentaje es: {0}".format(jugador_con_mejor_porcentaje))
        print("porcentaje de: {0}".format(maximo_porcentaje))
    else:
        print("No se encontró información de los jugadores.")

    
def jugador_con_mayor_cantidad_asistencias(lista_jugadores):
    maximo_asistencias = None
    jugador_con_mayor_asistencias = None

    for jugador in lista_jugadores:
        asistencias_tiros_de_campo = jugador["estadisticas"]["asistencias_totales"]
        if maximo_asistencias == None or asistencias_tiros_de_campo > maximo_asistencias:
            maximo_asistencias = asistencias_tiros_de_campo
            jugador_con_mayor_asistencias = jugador["nombre"]

    if jugador_con_mayor_asistencias is not None:
        print("El jugador con mejor asistencias es: {0}".format(jugador_con_mayor_asistencias))
        print("asistencias de: {0}".format(maximo_asistencias))
    else:
        print("No se encontró información de los jugadores.")

def jugador_con_mayor_puntos_por_partido(lista_jugadores):
    maximo_puntos= None
    jugador_con_mayor_puntos= None

    for jugador in lista_jugadores:
        promedio_puntos_por_jugador = jugador["estadisticas"]["promedio_puntos_por_partido"]
        if maximo_puntos== None or promedio_puntos_por_jugador > maximo_puntos:
            maximo_puntos= promedio_puntos_por_jugador
            jugador_con_mayor_puntos= jugador["nombre"]

    if jugador_con_mayor_puntos is not None:
        print("El jugador con mejor puntoses: {0}".format(jugador_con_mayor_puntos))
        print("puntosde: {0}".format(maximo_puntos))
    else:
        print("No se encontró información de los jugadores.")

'''

def jugador_con_mayor_estadistica(lista_jugadores, key, descripcion_estadistica):
    maximo_valor = None
    jugador_con_maximo_valor = None

    for jugador in lista_jugadores:
        valor_estadistica = jugador["estadisticas"][key]
        if maximo_valor is None or valor_estadistica > maximo_valor:
            maximo_valor = valor_estadistica
            jugador_con_maximo_valor = jugador["nombre"]

    if jugador_con_maximo_valor is not None:
        print("El jugador con el mayor {0} es: {1}".format(descripcion_estadistica, jugador_con_maximo_valor))
        print("{0}: {1}".format(descripcion_estadistica, maximo_valor))
    else:
        print("No se encontró información de los jugadores.")

'''
def mostrar_jugadores_mayor_promedio_puntos(lista_jugadores,valor_ingresado):
   
    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        promedio_puntos = jugador["estadisticas"]["promedio_puntos_por_partido"]
        if promedio_puntos > valor_ingresado:
            jugadores_seleccionados.append(jugador["nombre"])

    if jugadores_seleccionados:
        print("Jugadores con promedio de puntos por partido mayor a {0}:".format(valor_ingresado))
        for jugador in jugadores_seleccionados:
            print("- {0}".format(jugador))
    else:
        print("No se encontraron jugadores con promedio de puntos por partido mayor a {0}".format(valor_ingresado))

def mostrar_jugadores_mas_rebotes_promedio(lista_jugadores, valor_ingresado):
    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        promedio_rebotes = jugador["estadisticas"]["promedio_rebotes_por_partido"]
        if promedio_rebotes > valor_ingresado:
            jugadores_seleccionados.append(jugador["nombre"])

    if jugadores_seleccionados:
        print("Jugadores con promedio de rebotes por partido mayor a {0}:".format(valor_ingresado))
        for jugador in jugadores_seleccionados:
            print("- {0}".format(jugador))
    else:
        print("No se encontraron jugadores con promedio de rebotes por partido mayor a {0}".format(valor_ingresado))

def mostrar_jugadores_mas_asistencias_promedio(lista_jugadores, valor_ingresado):
    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        promedio_asistencias = jugador["estadisticas"]["promedio_asistencias_por_partido"]
        if promedio_asistencias > valor_ingresado:
            jugadores_seleccionados.append(jugador["nombre"])

    if jugadores_seleccionados:
        print("Jugadores con promedio de asistencias por partido mayor a {0}:".format(valor_ingresado))
        for jugador in jugadores_seleccionados:
            print("- {0}".format(jugador))
    else:
        print("No se encontraron jugadores con promedio de asistencias por partido mayor a {0}".format(valor_ingresado))

'''

def mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, key):
    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        promedio = jugador["estadisticas"][key]
        if promedio > valor_ingresado:
            jugadores_seleccionados.append(jugador["nombre"])

    if jugadores_seleccionados:
        print("Jugadores con promedio de {0} mayor a {1}:".format(key, valor_ingresado))
        for jugador in jugadores_seleccionados:
            print("- {0}".format(jugador))
    else:
        print("No se encontraron jugadores con promedio de {0} mayor a {1}".format(key, valor_ingresado))


def calcular_promedio_puntos_equipo_sin_el_mas_bajo(lista_jugadores):
    puntos_por_jugador = []

    # Calcular puntos por partido para cada jugador
    for jugador in lista_jugadores:
        puntos_totales = jugador["estadisticas"]["puntos_totales"]
        temporadas = jugador["estadisticas"]["temporadas"]
        puntos_por_partido = puntos_totales / temporadas
        puntos_por_jugador.append((jugador["nombre"], puntos_por_partido))

    # Encontrar al jugador con el menor promedio de puntos por partido
    jugador_menor_promedio = puntos_por_jugador[0]  # Suponemos que el primer jugador tiene el menor promedio
    for jugador in puntos_por_jugador:
        if jugador[1] < jugador_menor_promedio[1]:
            jugador_menor_promedio = jugador

    # Remover al jugador con el menor promedio de puntos por partido
    puntos_por_jugador.remove(jugador_menor_promedio)

    n = len(puntos_por_jugador)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if puntos_por_jugador[j][0] > puntos_por_jugador[j + 1][0]:
                puntos_por_jugador[j], puntos_por_jugador[j + 1] = puntos_por_jugador[j + 1], puntos_por_jugador[j]

    print("Promedio de puntos por partido del equipo del Dream Team:")
    for jugador in puntos_por_jugador:
        print("- {0}: {1}".format(jugador[0], jugador[1]))




