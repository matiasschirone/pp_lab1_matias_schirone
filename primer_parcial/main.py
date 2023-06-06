import json
from funciones import *
import re


def validar_opcion_menu(opcion):
    if re.match(r"^(0|[1-9]|1[0-9]|2[0-5])$", opcion):
        return True
    else:
        return False


while True:
    opcion = input("\n1- Mostrar la lista de jugadores\n2- Mostrar estadisticas de jugador\n3- Guardar estadisticas\n4- Mostrar logros de un jugador\n5- Promedio de puntos por partido\n6- Mostrar si pertenece al salón de la fama\n7- Jugador con mayor cantidad de rebotes\n8- Jugador con mayor porcentaje de tiros de campo\n9- Jugador con mayor cantidad de asistencias\n10- Jugadores que han promediado más puntos por partido\n11- Jugadores que han promediado más rebotes por partido\n12- Jugadores que han promediado más asistencias por partido\n13- Jugador con mayor cantidad de robos totales\n14- Jugador con mayor cantidad de bloqueos totales\n15- Jugadores que superan el porcentaje de tiros libres\n16- Promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos\n17- Jugador con mayor cantidad de logros obtenidos\n18- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior\n19- Jugador con la mayor cantidad de temporadas jugadas\n20- Ingresar un valor y mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior\n21- Cantidad de jugadores por cada poscicion\n22- Lista de jugadores en forma desc por cantidad de All Star\n23- Calcular de cada jugador cuál es su posición en puntos, rebotes, asistencias y robos\n24- Jugador tiene las mejores estadísticas en cada valor\n25- Jugador que tiene las mejores estadísticas de todos\n0 - Salir del programa\nIngrese la opción deseada: ")

    if validar_opcion_menu(opcion):

        respuesta_int = int(opcion)

        match respuesta_int:
            
            case 1:
                mostrar_lista_de_jugadores(lista_jugadores)
            case 2:
                seleccion = int(input("Selecciona un jugador por su índice: ")) - 1
                buscar_jugador(lista_jugadores, seleccion)
            case 3:
                jugador_seleccionado = lista_jugadores[seleccion]
                guardar_en_csv("jugador_seleccionado.csv", jugador_seleccionado)
            case 4:
                nombre_jugador = input("Ingrese el nombre (o parte del nombre) del jugador que desea buscar: ").lower()
                if re.match(r"^[a-zA-Z]+$",nombre_jugador):
                    buscar_jugador_por_nombre(lista_jugadores, nombre_jugador)                  
                else:
                    print("Ingrese solo letras. Inténtelo nuevamente.")          
            case 5:
                calcular_promedio_puntos_equipo(lista_jugadores)
            case 6:
                nombre_jugador = input("Ingrese el nombre del jugador: ")
                if re.match(r"^[a-zA-Z]+\s[a-zA-Z]+$", nombre_jugador):
                    verificar_miembro_hall_of_fame(lista_jugadores, nombre_jugador)
                else:
                    print("Ingrese solo letras y respete los espacios. Inténtelo nuevamente.")             
            case 7:
                jugador_con_mayor_estadistica(lista_jugadores, "rebotes_totales", "cantidad de rebotes totales")
            case 8:
                jugador_con_mayor_estadistica(lista_jugadores, "porcentaje_tiros_de_campo", "porcentaje de tiros de campo")
            case 9:
                jugador_con_mayor_estadistica(lista_jugadores, "asistencias_totales", "cantidad de asistencias")
            case 10:
                ingreso = input("Ingrese un valor de promedio de puntos por partido: ")
                if re.match(r"^\d+(\.\d+)?$", ingreso):
                    valor_ingresado = float(ingreso)
                    mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "promedio_puntos_por_partido")
                else:
                    print("Valor no válido. Intente nuevamente.")
            case 11:
                ingreso = input("Ingrese un valor de promedio de rebotes por partido: ")
                if re.match(r"^\d+(\.\d+)?$", ingreso):
                    valor_ingresado = float(ingreso)
                    mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "promedio_rebotes_por_partido")
                else:
                    print("Valor no válido. Intente nuevamente.")
            case 12:
                ingreso = input("Ingrese un valor de promedio de asistencias por partido: ")
                if re.match(r"^\d+(\.\d+)?$", ingreso):
                    valor_ingresado = float(ingreso)
                    mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "promedio_asistencias_por_partido")
                else:
                    print("Valor no válido. Intente nuevamente.")
            case 13:
                jugador_con_mayor_estadistica(lista_jugadores, "robos_totales", "robos totales")
            case 14:
                jugador_con_mayor_estadistica(lista_jugadores, "bloqueos_totales", "bloqueos totales")
            case 15:
                ingreso = input("Ingrese un valor de promedio de rebotes por partido: ")
                if re.match(r"^\d+(\.\d+)?$", ingreso):
                    valor_ingresado = float(ingreso)
                    mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "porcentaje_tiros_libres")
                else:
                    print("Valor no válido. Intente nuevamente.")
            case 16:
                calcular_promedio_puntos_equipo(lista_jugadores, excluir_jugador_bajo=True)
            case 17:
                jugador_con_mayor_logro(lista_jugadores, "logros", "logros")
            case 18:
                ingreso = input("Ingrese un valor de promedio de rebotes por partido: ")
                if re.match(r"^\d+(\.\d+)?$", ingreso):
                    valor_ingresado = float(ingreso)
                    mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "porcentaje_tiros_triples")
                else:
                    print("Valor no válido. Intente nuevamente.")
            case 19:
                jugador_con_mayor_estadistica(lista_jugadores, "temporadas", "temporadas")
            case 20:
                ingreso = input("Ingrese un valor de promedio de tiros de campo: ")
                if re.match(r"^\d+(\.\d+)?$", ingreso):
                    valor_ingresado = float(ingreso)
                    mostrar_jugadores_mayor_porcentaje_tiros_de_campo(lista_jugadores, valor_ingresado, "porcentaje_tiros_de_campo")
                else:
                    print("Valor no válido. Intente nuevamente.")
            case 21:
                jugadores_por_posicion = contar_jugadores_por_posicion(lista_jugadores)
                imprimir_dato(jugadores_por_posicion)
            case 22:
                mostrar_jugadores_por_all_star(lista_jugadores)   
            case 23:
                calcular_posiciones_ranking(lista_jugadores)
            case 24:
                obtener_mejores_estadisticas(lista_jugadores)
            case 25:
                mejor_jugador = obtener_mejor_jugador(lista_jugadores)
                for categoria in mejor_jugador:
                    resultado = mejor_jugador[categoria]
                    imprimir_dato(f"{categoria}: {resultado}")
                
            case 0:
                break

        #input("\nPulse enter para continuar\n")
    else:
        print("opcion no valida. intente buevamente")
    input("\nPulse enter para continuar\n")





            







