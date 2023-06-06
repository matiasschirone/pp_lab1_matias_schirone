
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
    La función "obtener_nombre" devuelve un mensaje de cadena con el nombre del jugador y la posición de
    una entrada de diccionario.
    
    :param dic_jugadores: Un diccionario que contiene información sobre un jugador, incluido su nombre y
    posición
    :return: una cadena que contiene el nombre y la posición de un jugador, obtenida de un diccionario
    de información de jugadores.
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
    La función "mostrar_lista_de_jugadores" toma una lista de jugadores e imprime sus nombres mediante
    las funciones "obtener_nombre" e "imprimir_dato".
    
    :param lista_jugadores: Una lista de jugadores, donde cada jugador se representa como un diccionario
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
    #seleccion = int(seleccion)

    if seleccion >= 0 and seleccion < len(lista_jugadores):
        jugador = lista_jugadores[seleccion]
        nombre = obtener_nombre(jugador)
        imprimir_dato(nombre)
        estadisticas = obtener_estadisticas(jugador)
        imprimir_dato(estadisticas)
    else: 
        imprimir_dato("El jugador no fue encontrado")

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


def buscar_jugador_por_nombre(lista_jugadores, nombre_jugador):
    """
    Esta función busca jugadores en una lista de jugadores por su nombre y devuelve una lista de
    jugadores coincidentes.
    
    :param lista_jugadores: una lista de diccionarios que representan a los jugadores, donde cada
    diccionario contiene información sobre un jugador, como su nombre, logros, etc
    :param nombre_jugador: El nombre del jugador que queremos buscar en la lista de jugadores
    :return: una lista de diccionarios que contienen información sobre los jugadores cuyos nombres
    coinciden con el nombre de entrada. Si no se encuentran coincidencias, se devuelve una lista vacía.
    """
    
    jugadores_coincidentes = []

    for jugador in lista_jugadores:
        if nombre_jugador.lower() in jugador["nombre"].lower():
            jugadores_coincidentes.append(jugador)

    if jugadores_coincidentes:
        imprimir_dato("Jugadores coincidentes:")
        for jugador in jugadores_coincidentes:
            nombre = obtener_nombre(jugador)
            imprimir_dato(nombre)
            logros = obtener_logros(jugador)
            imprimir_dato(logros)
    else:
        imprimir_dato("No se encontraron jugadores coincidentes")

    return jugadores_coincidentes


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

    imprimir_dato("No se encontró información del jugador {0}.".format(nombre_jugador).lower())


def jugador_con_mayor_estadistica(lista_jugadores, key, descripcion_estadistica):
    """
    Esta función encuentra al jugador con el valor más alto para una estadística dada e imprime su
    nombre y el valor.
    
    :param lista_jugadores: Una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene información sobre su nombre y estadísticas
    :param key: La clave es una cadena que representa la estadística específica que queremos comparar
    entre los jugadores. Por ejemplo, pueden ser "puntos" (puntos), "rebotes" (rebotes), "asistencias"
    (asistencias), etc
    :param descripcion_estadistica: una cadena que describe la estadística que se analiza (por ejemplo,
    "puntos", "rebotes", "asistencias")
    """
    maximo_valor = None
    jugador_con_maximo_valor = None

    for jugador in lista_jugadores:
        valor_estadistica = jugador["estadisticas"][key]
        if maximo_valor is None or valor_estadistica > maximo_valor:
            maximo_valor = valor_estadistica
            jugador_con_maximo_valor = jugador["nombre"]

    if jugador_con_maximo_valor is not None:
        imprimir_dato("El jugador con el mayor {0} es: {1}".format(descripcion_estadistica, jugador_con_maximo_valor))
        imprimir_dato("{0}: {1}".format(descripcion_estadistica, maximo_valor))
    else:
        imprimir_dato("No se encontró información de los jugadores.")

def jugador_con_mayor_logro(lista_jugadores, key, descripcion):
    """
    Esta función encuentra al jugador con el mayor número de logros en una lista de jugadores e imprime
    su nombre y el número de logros.
    
    :param lista_jugadores: Una lista de diccionarios que representan a diferentes jugadores, donde cada
    diccionario contiene información sobre un jugador, como su nombre, logros, etc
    :param key: El parámetro clave no se utiliza en la función dada. No es necesario para que la función
    funcione correctamente
    :param descripcion: una cadena que describe el tipo de logro que se compara (por ejemplo, "puntos",
    "goles", "asistencias")
    """
    maximo_valor = None
    jugador_con_mayor_logro = None

    for jugador in lista_jugadores:
        logros = jugador["logros"]
        valor_logros = len(logros)  # Obtenemos la cantidad de logros del jugador

        if maximo_valor is None or valor_logros > maximo_valor:
            maximo_valor = valor_logros
            jugador_con_mayor_logro = jugador["nombre"]

    if jugador_con_mayor_logro is not None:
        imprimir_dato("El jugador con la mayor cantidad de {0} es: {1}".format(descripcion, jugador_con_mayor_logro))
        imprimir_dato("Cantidad de {0}: {1}".format(descripcion, maximo_valor))
    else:
        imprimir_dato("No se encontró información de los jugadores.")


def mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, key):
    """
    La función selecciona y muestra los nombres de los jugadores cuyas estadísticas cumplen con ciertos
    criterios.
    
    :param lista_jugadores: una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas
    :param valor_ingresado: El valor ingresado por el usuario para comparar con las estadísticas
    promedio de los jugadores
    :param key: La clave es una cadena que representa la estadística que queremos comparar con el valor
    ingresado por el usuario. Por ejemplo, si el usuario ingresa un valor de 10 y la clave es "puntos",
    la función buscará jugadores cuyo promedio de puntos por juego sea mayor a 10
    :return: una lista de los nombres de los jugadores cuyas estadísticas cumplen la condición de tener
    un promedio superior al valor ingresado por el usuario.
    """
    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        promedio = jugador["estadisticas"][key]
        if promedio > valor_ingresado:
            jugadores_seleccionados.append(jugador["nombre"])

    if jugadores_seleccionados:
        imprimir_dato("Jugadores con promedio de {0} mayor a {1}:".format(key, valor_ingresado))
        for jugador in jugadores_seleccionados:
            imprimir_dato("- {0}".format(jugador))
    else:
        imprimir_dato("No se encontraron jugadores con promedio de {0} mayor a {1}".format(key, valor_ingresado))

    return jugadores_seleccionados


'''
def ordenar_por_atributo(lista, atributo):
    """
    Esta función ordena una lista de diccionarios por un atributo dado.

    :param lista: una lista de diccionarios que se desea ordenar.
    :param atributo: el nombre del atributo por el cual se desea ordenar la lista.
    :return: la función devuelve una lista de diccionarios `lista` ordenados por el valor del atributo especificado.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j][atributo] > lista[j + 1][atributo]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
'''

def ordenar_por_atributo(lista, atributo, ascendente=True):
    """
    Esta función ordena una lista de diccionarios por un atributo dado.

    :param lista: una lista de diccionarios que se desea ordenar.
    :param atributo: el nombre del atributo por el cual se desea ordenar la lista.
    :param ascendente: un valor booleano que indica si el ordenamiento debe ser ascendente (True) o descendente (False).
    :return: la función devuelve una lista de diccionarios `lista` ordenados por el valor del atributo especificado.
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if ascendente:
                if lista[j][atributo] > lista[j + 1][atributo]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j][atributo] < lista[j + 1][atributo]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista



def calcular_promedio_puntos_equipo(lista_jugadores, excluir_jugador_bajo=False):
    """
    Esta función calcula el promedio de puntos por juego para cada jugador en una lista dada de
    jugadores y puede excluir opcionalmente al jugador con el promedio más bajo.

    :param lista_jugadores: Una lista de diccionarios, donde cada diccionario representa a un jugador y
    contiene su nombre y estadísticas (puntos totales y temporadas jugadas)
    :param excluir_jugador_bajo: Este es un parámetro booleano que determina si se excluye o no al
    jugador con el promedio de puntos por juego más bajo del cálculo del promedio de puntos por juego
    del equipo. Si se establece en True, la función excluirá al jugador con el promedio de puntos más
    bajo por juego. Si se establece en falso, defaults to False (optional)
    """
    puntos_por_jugador = []

    # Calcular puntos por partido para cada jugador
    for jugador in lista_jugadores:
        puntos_totales = jugador["estadisticas"]["puntos_totales"]
        temporadas = jugador["estadisticas"]["temporadas"]
        puntos_por_partido = puntos_totales / temporadas
        puntos_por_jugador.append({"nombre": jugador["nombre"], "puntos_por_partido": puntos_por_partido})

    # Encontrar al jugador con el menor promedio de puntos por partido
    if excluir_jugador_bajo:
        puntos_por_jugador = ordenar_por_atributo(puntos_por_jugador, "puntos_por_partido")
        puntos_por_jugador = puntos_por_jugador[1:]  # Excluir al jugador con el menor promedio

    # Ordenar la lista por nombre del jugador
    puntos_por_jugador = ordenar_por_atributo(puntos_por_jugador, "nombre")

    # Mostrar promedio de puntos por partido para todo el equipo
    if excluir_jugador_bajo:
        imprimir_dato("Promedio de puntos por partido del equipo del Dream Team (excluyendo al jugador con menor promedio):")
    else:
        imprimir_dato("Promedio de puntos por partido del equipo del Dream Team:")

    for jugador in puntos_por_jugador:
        imprimir_dato("- {0}: {1}".format(jugador["nombre"], jugador["puntos_por_partido"]))


def ordenar_por_posicion(jugadores):
    """l
    Esta función ordena una lista de diccionarios de jugadores por su atributo de posición.

    :param jugadores: una lista de diccionarios que representan a los jugadores de un equipo deportivo,
    donde cada diccionario contiene información sobre el jugador, como su nombre, posición y
    estadísticas. La función ordena la lista de jugadores por su posición en orden ascendente y devuelve
    la lista ordenada
    :return: La función `ordenar_por_posicion` devuelve una lista de diccionarios `jugadores` ordenados
    por el valor de la clave "posicion" en orden ascendente.
    """
    return ordenar_por_atributo(jugadores, "posicion")


def mostrar_jugadores_mayor_porcentaje_tiros_de_campo(lista_jugadores, valor_ingresado, key):
    """
    Esta función selecciona y muestra los nombres de los jugadores de baloncesto con un porcentaje de
    tiro superior a un valor determinado.
    
    :param lista_jugadores: una lista de diccionarios que representan a los jugadores de baloncesto,
    cada uno con sus propias estadísticas
    :param valor_ingresado: Un valor numérico que representa el umbral mínimo para la estadística
    seleccionada (clave)
    :param key: El parámetro clave es una cadena que representa la estadística que se utilizará para
    filtrar la lista de jugadores. Se utiliza para acceder al valor correspondiente en el diccionario de
    estadísticas de cada jugador
    """
    jugadores_seleccionados = []

    for jugador in lista_jugadores:
        promedio = jugador["estadisticas"][key]
        if promedio > valor_ingresado:
            jugadores_seleccionados.append(jugador)

    if jugadores_seleccionados:

        jugadores_seleccionados = ordenar_por_posicion(jugadores_seleccionados)

        for jugador in jugadores_seleccionados:
                nombre = obtener_nombre(jugador)
                imprimir_dato(nombre)
    else:
        imprimir_dato("No se encontraron jugadores con promedio de {0} mayor a {1}".format(key, valor_ingresado))


def calcular_posiciones_ranking(lista_jugadores):
    n = len(lista_jugadores)

    posiciones_puntos = [0] * n
    posiciones_rebotes = [0] * n
    posiciones_asistencias = [0] * n
    posiciones_robos = [0] * n

    for i in range(n):
        puntos_jugador = lista_jugadores[i]["estadisticas"]["puntos_totales"]
        rebotes_jugador = lista_jugadores[i]["estadisticas"]["rebotes_totales"]
        asistencias_jugador = lista_jugadores[i]["estadisticas"]["asistencias_totales"]
        robos_jugador = lista_jugadores[i]["estadisticas"]["robos_totales"]

        for j in range(n):
            if puntos_jugador > lista_jugadores[j]["estadisticas"]["puntos_totales"]:
                posiciones_puntos[i] += 1
            if rebotes_jugador > lista_jugadores[j]["estadisticas"]["rebotes_totales"]:
                posiciones_rebotes[i] += 1
            if asistencias_jugador > lista_jugadores[j]["estadisticas"]["asistencias_totales"]:
                posiciones_asistencias[i] += 1
            if robos_jugador > lista_jugadores[j]["estadisticas"]["robos_totales"]:
                posiciones_robos[i] += 1

    archivo_salida = "ranking.csv"

    with open(archivo_salida, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Jugador", "Puntos", "Rebotes", "Asistencias", "Robos"])

        for i in range(n):
            jugador = lista_jugadores[i]["nombre"]
            posicion_puntos = posiciones_puntos[i] + 1
            posicion_rebotes = posiciones_rebotes[i] + 1
            posicion_asistencias = posiciones_asistencias[i] + 1
            posicion_robos = posiciones_robos[i] + 1

            writer.writerow([jugador, posicion_puntos, posicion_rebotes, posicion_asistencias, posicion_robos])

        # Agregar una fila vacía para separar el encabezado del cuerpo del cuadro
        writer.writerow([])

    return archivo_salida


def contar_jugadores_por_posicion(lista_jugadores):
    jugadores_por_posicion = {}

    for jugador in lista_jugadores:
        posicion = jugador["posicion"]

        if posicion in jugadores_por_posicion:
            jugadores_por_posicion[posicion] += 1
        else:
            jugadores_por_posicion[posicion] = 1

    return jugadores_por_posicion

import json

def mostrar_jugadores_por_all_star(lista_jugadores):
    jugadores_ordenados = []
    for jugador in lista_jugadores:
        all_star = 0
        for logro in jugador['logros']:
            if 'All-Star' in logro:
                # Extraer la cantidad de All-Star del logro
                all_star = int(logro.split()[0])  # Ejemplo: '14 veces All-Star' -> 14
                break  # Solo se necesita el primer logro de All-Star
        jugador['all_star'] = all_star
        jugadores_ordenados.append(jugador)

    # Ordenar los jugadores por la cantidad de All-Star de forma descendente
    for i in range(len(jugadores_ordenados)):
        for j in range(i + 1, len(jugadores_ordenados)):
            if jugadores_ordenados[i]['all_star'] < jugadores_ordenados[j]['all_star']:
                jugadores_ordenados[i], jugadores_ordenados[j] = jugadores_ordenados[j], jugadores_ordenados[i]

    # Mostrar los jugadores ordenados por la cantidad de All-Star
    for jugador in jugadores_ordenados:
        nombre = jugador['nombre']
        all_star = jugador['all_star']
        logros_all_star = f"{all_star} veces All-Star"
        imprimir_dato(f"{nombre} ({logros_all_star})")

    return jugadores_ordenados


def obtener_mejores_estadisticas(lista_jugadores):
    mejor_temporadas = None
    mejor_puntos_totales = None
    mejor_promedio_puntos = None
    mejor_rebotes_totales = None
    mejor_promedio_rebotes = None
    mejor_asistencias_totales = None
    mejor_promedio_asistencias = None
    mejor_robos_totales = None
    mejor_bloqueos_totales = None
    mejor_porcentaje_tiros_campo = None
    mejor_porcentaje_tiros_libres = None
    mejor_porcentaje_tiros_triples = None

    for jugador in lista_jugadores:
        estadisticas = jugador['estadisticas']

        if mejor_temporadas is None or estadisticas['temporadas'] > mejor_temporadas['estadisticas']['temporadas']:
            mejor_temporadas = jugador

        if mejor_puntos_totales is None or estadisticas['puntos_totales'] > mejor_puntos_totales['estadisticas']['puntos_totales']:
            mejor_puntos_totales = jugador

        if mejor_promedio_puntos is None or estadisticas['promedio_puntos_por_partido'] > mejor_promedio_puntos['estadisticas']['promedio_puntos_por_partido']:
            mejor_promedio_puntos = jugador

        if mejor_rebotes_totales is None or estadisticas['rebotes_totales'] > mejor_rebotes_totales['estadisticas']['rebotes_totales']:
            mejor_rebotes_totales = jugador

        if mejor_promedio_rebotes is None or estadisticas['promedio_rebotes_por_partido'] > mejor_promedio_rebotes['estadisticas']['promedio_rebotes_por_partido']:
            mejor_promedio_rebotes = jugador

        if mejor_asistencias_totales is None or estadisticas['asistencias_totales'] > mejor_asistencias_totales['estadisticas']['asistencias_totales']:
            mejor_asistencias_totales = jugador

        if mejor_promedio_asistencias is None or estadisticas['promedio_asistencias_por_partido'] > mejor_promedio_asistencias['estadisticas']['promedio_asistencias_por_partido']:
            mejor_promedio_asistencias = jugador

        if mejor_robos_totales is None or estadisticas['robos_totales'] > mejor_robos_totales['estadisticas']['robos_totales']:
            mejor_robos_totales = jugador

        if mejor_bloqueos_totales is None or estadisticas['bloqueos_totales'] > mejor_bloqueos_totales['estadisticas']['bloqueos_totales']:
            mejor_bloqueos_totales = jugador

        if mejor_porcentaje_tiros_campo is None or estadisticas['porcentaje_tiros_de_campo'] > mejor_porcentaje_tiros_campo['estadisticas']['porcentaje_tiros_de_campo']:
            mejor_porcentaje_tiros_campo = jugador

        if mejor_porcentaje_tiros_libres is None or estadisticas['porcentaje_tiros_libres'] > mejor_porcentaje_tiros_libres['estadisticas']['porcentaje_tiros_libres']:
            mejor_porcentaje_tiros_libres = jugador

        if mejor_porcentaje_tiros_triples is None or estadisticas['porcentaje_tiros_triples'] > mejor_porcentaje_tiros_triples['estadisticas']['porcentaje_tiros_triples']:
            mejor_porcentaje_tiros_triples = jugador

    # Mostrar los jugadores con las mejores estadísticas
    imprimir_dato(f"Mayor cantidad de temporadas: {mejor_temporadas['nombre']} ({mejor_temporadas['estadisticas']['temporadas']})")
    imprimir_dato(f"Mayor cantidad de puntos totales: {mejor_puntos_totales['nombre']} ({mejor_puntos_totales['estadisticas']['puntos_totales']})")
    imprimir_dato(f"Mayor promedio de puntos por partido: {mejor_promedio_puntos['nombre']} ({mejor_promedio_puntos['estadisticas']['promedio_puntos_por_partido']})")
    imprimir_dato(f"Mayor cantidad de rebotes totales: {mejor_rebotes_totales['nombre']} ({mejor_rebotes_totales['estadisticas']['rebotes_totales']})")
    imprimir_dato(f"Mayor promedio de rebotes por partido: {mejor_promedio_rebotes['nombre']} ({mejor_promedio_rebotes['estadisticas']['promedio_rebotes_por_partido']})")
    imprimir_dato(f"Mayor cantidad de asistencias totales: {mejor_asistencias_totales['nombre']} ({mejor_asistencias_totales['estadisticas']['asistencias_totales']})")
    imprimir_dato(f"Mayor promedio de asistencias por partido: {mejor_promedio_asistencias['nombre']} ({mejor_promedio_asistencias['estadisticas']['promedio_asistencias_por_partido']})")
    imprimir_dato(f"Mayor cantidad de robos totales: {mejor_robos_totales['nombre']} ({mejor_robos_totales['estadisticas']['robos_totales']})")
    imprimir_dato(f"Mayor cantidad de bloqueos totales: {mejor_bloqueos_totales['nombre']} ({mejor_bloqueos_totales['estadisticas']['bloqueos_totales']})")
    imprimir_dato(f"Mayor porcentaje de tiros de campo: {mejor_porcentaje_tiros_campo['nombre']} ({mejor_porcentaje_tiros_campo['estadisticas']['porcentaje_tiros_de_campo']})")
    imprimir_dato(f"Mayor porcentaje de tiros libres: {mejor_porcentaje_tiros_libres['nombre']} ({mejor_porcentaje_tiros_libres['estadisticas']['porcentaje_tiros_libres']})")
    imprimir_dato(f"Mayor porcentaje de tiros triples: {mejor_porcentaje_tiros_triples['nombre']} ({mejor_porcentaje_tiros_triples['estadisticas']['porcentaje_tiros_triples']})")


def obtener_mejor_jugador(lista_jugadores):
    mejor_temporadas = None
    mejor_puntos_totales = None
    mejor_rebotes_totales = None
    mejor_asistencias_totales = None

    for jugador in lista_jugadores:
        if mejor_temporadas is None or jugador['estadisticas']['temporadas'] > mejor_temporadas['estadisticas']['temporadas']:
            mejor_temporadas = jugador

        if mejor_puntos_totales is None or jugador['estadisticas']['puntos_totales'] > mejor_puntos_totales['estadisticas']['puntos_totales']:
            mejor_puntos_totales = jugador

        if mejor_rebotes_totales is None or jugador['estadisticas']['rebotes_totales'] > mejor_rebotes_totales['estadisticas']['rebotes_totales']:
            mejor_rebotes_totales = jugador

        if mejor_asistencias_totales is None or jugador['estadisticas']['asistencias_totales'] > mejor_asistencias_totales['estadisticas']['asistencias_totales']:
            mejor_asistencias_totales = jugador

    resultado = {
        'Mayor cantidad de temporadas': mejor_temporadas['nombre'] + ' (' + str(mejor_temporadas['estadisticas']['temporadas']) + ')',
        'Mayor cantidad de puntos totales': mejor_puntos_totales['nombre'] + ' (' + str(mejor_puntos_totales['estadisticas']['puntos_totales']) + ')',
        'Mayor cantidad de rebotes totales': mejor_rebotes_totales['nombre'] + ' (' + str(mejor_rebotes_totales['estadisticas']['rebotes_totales']) + ')',
        'Mayor cantidad de asistencias totales': mejor_asistencias_totales['nombre'] + ' (' + str(mejor_asistencias_totales['estadisticas']['asistencias_totales']) + ')'
    }

    return resultado
    imprimir_dato(resultado)




'''
Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente. La salida por pantalla debe tener un formato similar a este:
Michael Jordan (14 veces All Star)
Magic Johnson (12 veces All-Star)
...

Determinar qué jugador tiene las mejores estadísticas en cada valor. La salida por pantalla debe tener un formato similar a este:
Mayor cantidad de temporadas: Karl Malone (19)
Mayor cantidad de puntos totales: Karl Malon (36928)
…

Determinar qué jugador tiene las mejores estadísticas de todos.

'''






