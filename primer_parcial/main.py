import json
from funciones import *
            


while True:
    opcion = input("\n1- Mostrar la lista de jugadores\n2- Mostrar estadisticas de jugador\n3- Guardar estadisticas\n4- ostrar logros de un jugador\n5- promedio de puntos por partido\n6-Mostrar si pertenece al salon de la fama\n7- Jugador con mayor cantidad de rebotes\n8-Jugador con mayor porcenaje tiros de campo\n9- Jugador con mayor cantidad de asistencias\n10- Jugadores que han promediado mas puntos por partido\n11- Jugadores que han promediado mas rebotes por partido\n12- Jugadores que han promediado mas asistencias por partido\n13- Jugador con mayor cantidad de robos totales\n14- Jugador con mayor cantidad de bloqueos totales\n15- Jugadores que que superan el porcentaje de tiros libres\n16- Promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos\n17- Jugador con mayor cantidad de logros obtenidos\n18- Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior\n19- Jugador con la mayor cantidad de temporadas jugadas\n20- ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior\n0- Salir del programa\nIngrese la opción deseada: ")
        

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
            jugador_con_mayor_estadistica(lista_jugadores, "rebotes_totales", "cantidad de rebotes totales")
        case 8:
            jugador_con_mayor_estadistica(lista_jugadores, "porcentaje_tiros_de_campo", "porcentaje de tiros de campo")
        case 9:
            jugador_con_mayor_estadistica(lista_jugadores, "asistencias_totales", "cantidad de asistencias")
        case 10:
            ingreso = input("Ingrese un valor de promedio de puntos por partido: ")
            valor_ingresado = float(ingreso)
            mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado,"promedio_puntos_por_partido")
        case 11:
            ingreso = input("Ingrese un valor de promedio de rebotes por partido: ")
            valor_ingresado = float(ingreso)
            mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "promedio_rebotes_por_partido")
        case 12:
            ingreso = input("Ingrese un valor de promedio de asistencias por partido: ")
            valor_ingresado = float(ingreso)
            mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "promedio_asistencias_por_partido")
        case 13:
            jugador_con_mayor_estadistica(lista_jugadores, "robos_totales", "robos totales")
        case 14:
            jugador_con_mayor_estadistica(lista_jugadores, "bloqueos_totales", "bloqueos totales")
        case 15:
            ingreso = input("Ingrese un valor de promedio de rebotes por partido: ")
            valor_ingresado = float(ingreso)
            mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "porcentaje_tiros_libres")
        case 16:
            calcular_promedio_puntos_equipo(lista_jugadores, excluir_jugador_bajo=True)
        case 17:
            jugador_con_mayor_logro(lista_jugadores, "logros", "logros")
        case 18:
            ingreso = input("Ingrese un valor de promedio de rebotes por partido: ")
            valor_ingresado = float(ingreso)
            mostrar_jugadores_mayor_promedio(lista_jugadores, valor_ingresado, "porcentaje_tiros_triples")
        case 19:
            jugador_con_mayor_estadistica(lista_jugadores, "temporadas", "temporadas")
        case 20:
            ingreso = input("Ingrese un valor de promedio de tiros de campo: ")
            valor_ingresado = float(ingreso)
            mostrar_jugadores_mayor_porcentaje_tiros_de_campo(lista_jugadores, valor_ingresado, "porcentaje_tiros_de_campo")
        case 0:
            break
    

    input("\nPulse enter para continuar\n")







