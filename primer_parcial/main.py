import json
from funciones import *
            


while True:
    opcion = input("\n1- Mostrar la lista de jugadores\n2- Mostrar estadisticas de jugador\n3- Guardar estadisticas\n4- ostrar logros de un jugador\n5- promedio de puntos por partido\n6-Mostrar si pertenece al salon de la fama\n7- Jugador con mayor cantidad de rebotes\n8-Jugador con mayor porcenaje tiros de campo\n9- Jugador con mayor cantidad de asistencias\n10- Jugadores que han promediado mas puntos por partido\n11- Jugadores que han promediado mas rebotes por partido\n12- Jugadores que han promediado mas asistencias por partido\n13- Jugador con mayor cantidad de robos totales\n14- Jugador con mayor cantidad de bloqueos totales\n15- Jugadores que que superan el porcentaje de tiros libres\n16- Promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos\n17- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior\n19- Jugador con la mayor cantidad de temporadas jugadas\n20- ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior\n0- Salir del programa\nIngrese la opción deseada: ")
        

    respuesta_int = int(opcion)

    
    match(respuesta_int):
        case 1:
           mostrar_lista_de_jugadores(lista_jugadores)
        case 2:
            seleccion = int(input("Selecciona un jugador por su índice: ")) - 1
            buscar_jugador(lista_jugadores,seleccion)
        case 3:
            jugador_seleccionado = lista_jugadores[seleccion]
            guardar_en_csv("jugador_seleccionado.csv", jugador_seleccionado)
        case 4:            
            nombre_jugador = input("Ingrese el nombre (o parte del nombre) del jugador que desea buscar: ").lower()
            buscar_jugador_por_nombre(lista_jugadores, nombre_jugador)
        case 5:
           calcular_promedio_puntos_equipo(lista_jugadores)
        case 6:
            nombre_jugador = input("Ingrese el nombre del jugador: ")
            verificar_miembro_hall_of_fame(lista_jugadores,nombre_jugador)
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            pass
        case 14:
            pass
        case 15:
            pass
        case 16:
            pass
        case 17:
            pass
        case 18:
            pass
        case 19:
            pass
        case 20:
            pass
        case 0:
            break
    

    input("\nPulse enter para continuar\n")







