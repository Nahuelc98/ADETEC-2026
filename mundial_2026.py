from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador
from simulador_partidos import simular_partido
from mundial_db import conectar, eliminar_seleccion, mostrar_selecciones, agregar_seleccion ,agregar_jugador, sacar_jugador, mostrar_plantel
import random
import time

# # FUNCIÓN ESCRIBIR EN ARCHIVO:
# def escribir_archivo(nombre_archivo, texto):
#     archivo = open(nombre_archivo, "a", encoding="utf-8")
#     archivo.write(texto)
#     archivo.close()

# # FUNCIÓN REESCRIBIR ARCHIVO:
# def reescribir_archivo(nombre_archivo, lineas):
#     archivo = open(nombre_archivo, "w", encoding="utf-8")
#     archivo.writelines(lineas)
#     archivo.close()

# # FUNCIÓN LEER ARCHIVO:
# def leer_archivo(nombre_archivo):
#     archivo = open(nombre_archivo, "r", encoding="utf-8")
#     contenido = archivo.readlines()
#     archivo.close()
#     return contenido

# # FUNCIÓN PARA CARGAR EL ARCHIVO EN MEMORIA:
# def cargar_plantel(seleccion, nombre_archivo):
#     seleccion.convocados.clear()
#     lineas = leer_archivo(nombre_archivo)
#     for linea in lineas:
#         linea = linea.strip()
#         if linea:
#             datos = linea.split(",")
#             if len(datos) >= 4:
#                 nombre, apellido, posicion, numero = datos[0], datos[1], datos[2], datos[3]
#                 jugador = Jugador(nombre, apellido, posicion, numero)
#                 seleccion.convocar(jugador)

# # Crear selecciones:
# sel_argentina = SeleccionFutbol("Argentina","Lionel Scaloni",3,"A")
# sel_española = SeleccionFutbol("España","Luis de la Fuente",2,"A")
# sel_francesa = SeleccionFutbol("Francia","Zinédine Zidane",2,"A")
# sel_inglesa = SeleccionFutbol("Inglaterra","Thomas Tuchel",1,"A")

# # Cargar el equipo guardado previamente al arrancar el programa:
# cargar_plantel(sel_argentina, "plantel_argentina.txt")
# cargar_plantel(sel_española, "plantel_españa.txt")
# cargar_plantel(sel_francesa, "plantel_francia.txt")
# cargar_plantel(sel_inglesa, "plantel_inglaterra.txt")

# Conectamos localmente:
conexion = conectar('127.0.0.1', 'root', 3306)

# Inicio del mundial:
print("BIENVENIDO AL MUNDIAL 2026")
print("-" * 25)

# Menú principal:
while True:
    print("\nMENÚ PRINCIPAL")
    print("-" * 25)
    print("1. Gestionar selecciones")
    print("2. Completar planteles")
    print("3. Simular partidos")
    print("4. Salir")

    opcion = input("Selecciona una opción [1, 2, 3 o 4]: ")

    # Cierre del bucle pricipal:
    if opcion == "4":
        print("\nMUNDIAL FINALIZADO\n")
        break
    # Opción de gestionar selecciones:
    elif opcion == "1":
        # Bucle de gestionar selecciones:
        while True:
            print("\nMenú: Gestionar Selecciones")
            print("-" * 30)
            print("1. Lista de selecciones")
            print("2. Agregar selecciones")
            print("3. Quitar selecciones")
            print("4. Volver al menú pricipal")

            opcion_seleccion = input("\nSelecciona una opción [1, 2, 3 o 4]: ")

            if opcion_seleccion == "4":
                print("GESTIÓN DE SELECCIONES FINALIZADA")
                break
            elif opcion_seleccion == "1":
                mostrar_selecciones(conexion)
            elif opcion_seleccion == "2":
                 s_cantidad = int(input("\n¿Cuántas selecciones vas a agregar? [Ingresa 0 para cancelar] "))
                 for i in range(s_cantidad):
                    print(f"\nSelección {i+1}:")
                    agregar_seleccion(conexion)
            elif opcion_seleccion == "3":
                s_cantidad_quitar = int(input("\n¿Cuántas selecciones vas a eliminar? [Ingresa 0 para cancelar] "))
                for i in range(s_cantidad_quitar):
                    print(f"\nSelección {i+1} a eliminar:")
                    eliminar_seleccion(conexion)
            else:
                print("OPCIÓN INCORRECTA")

    # Opción de completar planteles:
    elif opcion == "2":
        mostrar_selecciones(conexion)
        print("¿Con que selección vas a trabajar?")
        equipo = input("Ingresa el nombre de la selección: ").strip().capitalize()   
    # Bucle de completar planteles: 
        while True:
            print(f"\n - SELECCIÓN DE {equipo.upper()} -")
            print("\nMenú: Completar planteles")
            print("-" * 30)
            print("1. Mostrar equipo")
            print("2. Convocar jugador")
            print("3. Quitar jugador")
            print("4. Volver al menú principal")

            opcion_plantel = input("Seleccioná una opción [1, 2, 3 o 4]: ")
            # Cierre del bucle completar planteles:
            if opcion_plantel == "4":
                print(f"SELECCIÓN DEL PLANTEL DE {equipo.upper()} FINALIZADA")
                break
            # Mostrar equipo actual:
            elif opcion_plantel == "1":
                mostrar_plantel(conexion, equipo)
            # Convocar jugadores:
            elif opcion_plantel == "2":
                cantidad = int(input("\n¿Cuántos jugadores vas a convocar? [Ingresa 0 para cancelar] "))
                
                for i in range(cantidad):
                    print(f"\nJugador {i+1}:")
                    agregar_jugador(conexion, equipo)

            # Quitar jugadores:
            elif opcion_plantel == "3":
                cantidad_quitar = int(input("\n¿Cuantos jugadores vas a quitar? [Ingresa 0 para cancelar] "))

                for i in range(cantidad_quitar):
                    print(f"\nJugador {i+1} a quitar:")
                    sacar_jugador(conexion,equipo)

            else:
                print("\nOPCIÓN INCORRECTA\n")

    # Opción de simular partidos:
    elif opcion == "3":
        while True:
            print("\nSIMULACIÓN DE PARTIDOS")
            print("\nMenú: Partidos")
            print("-" * 25)
            print("1. Simular partidos")
            print("2. Volver al menú principal")

            opcion_simular = input("Seleccioná una opción [1 o 2]: ")

            if opcion_simular == "2":
                print("Simulación de partidos, cerrada")
                break

            elif opcion_simular == "1":
                selecciones_futbol = ["Argentina", "España", "Francia", "Inglaterra"]

                # Mezclamos la lista completa de forma aleatoria:
                random.shuffle(selecciones_futbol)

                # Le asignamos los 4 equipos directamente en las variables:
                semifinalista_1, semifinalista_2, semifinalista_3, semifinalista_4 = selecciones_futbol

                print("\nSORTEO DE SEMIFINALES...\n")
                time.sleep(3)
                print(f"Semifinal 1: {semifinalista_1} vs {semifinalista_2}")
                print(f"Semifinal 2: {semifinalista_3} vs {semifinalista_4}")
                time.sleep(3)

                print(f"\nCOMIENZA LA PRIMER SEMIFINAL...\n")
                ganador, perdedor = simular_partido(semifinalista_1, semifinalista_2)
                print(f"\nEL PRIMER FINALISTA ES {ganador.upper()}\n")
                time.sleep(3)
                finalista1 = ganador
                tercero1 = perdedor

                print(f"\nCOMIENZA LA SEGUNDA SEMIFINAL...\n")
                ganador, perdedor = simular_partido(semifinalista_3, semifinalista_4)
                print(f"\nEL SEGUNDO FINALISTA ES {ganador.upper()}\n")
                time.sleep(3)
                finalista2 = ganador
                tercero2 = perdedor

                print(f"\nCOMIENZA EL PARTIDO POR EL TERCER PUESTO...\n")
                ganador, perdedor = simular_partido(tercero1, tercero2)
                print(f"\nAL TERCER PUESTO SE LO QUEDA {ganador.upper()}\n") 

                print(f"\nCOMIENZA LA FINAL DEL MUNDIAL...\n")
                ganador, perdedor = simular_partido(finalista1, finalista2)
                print(f"\nSUBCAMPEÓN: {perdedor.upper()}")
                print(f"\nEL CAMPEÓN DEL MUNDO ES {ganador.upper()}\n")

                print("\n-- Fin de la simulación --\n")               

    else:
        print("\nOPCIÓN INCORRECTA\n")

conexion.close()