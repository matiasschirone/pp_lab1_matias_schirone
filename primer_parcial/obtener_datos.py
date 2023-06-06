
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
    return ordenar_por_atributo(jugadores, "posicion",True)
