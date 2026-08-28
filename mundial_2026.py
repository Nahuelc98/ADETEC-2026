from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador
from simulador_partidos import simular_partido
import random
import time

# FUNCIÓN ESCRIBIR EN ARCHIVO:
def escribir_archivo(nombre_archivo, texto):
    archivo = open(nombre_archivo, "a", encoding="utf-8")
    archivo.write(texto)
    archivo.close()

# FUNCIÓN REESCRIBIR ARCHIVO:
def reescribir_archivo(nombre_archivo, lineas):
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    archivo.writelines(lineas)
    archivo.close()

# FUNCIÓN LEER ARCHIVO:
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contenido = archivo.readlines()
    archivo.close()
    return contenido

# FUNCIÓN PARA CARGAR EL ARCHIVO EN MEMORIA:
def cargar_plantel(seleccion, nombre_archivo):
    seleccion.convocados.clear()
    lineas = leer_archivo(nombre_archivo)
    for linea in lineas:
        linea = linea.strip()
        if linea:
            datos = linea.split(",")
            if len(datos) >= 4:
                nombre, apellido, posicion, numero = datos[0], datos[1], datos[2], datos[3]
                jugador = Jugador(nombre, apellido, posicion, numero)
                seleccion.convocar(jugador)

# Crear selecciones:
sel_argentina = SeleccionFutbol("Argentina","Lionel Scaloni",3,"A")
sel_española = SeleccionFutbol("España","Luis de la Fuente",2,"A")
sel_francesa = SeleccionFutbol("Francia","Zinédine Zidane",2,"A")
sel_inglesa = SeleccionFutbol("Inglaterra","Thomas Tuchel",1,"A")

# Cargar el plantel guardado previamente al arrancar el programa:
cargar_plantel(sel_argentina, "plantel_argentina.txt")
cargar_plantel(sel_española, "plantel_españa.txt")
cargar_plantel(sel_francesa, "plantel_francia.txt")
cargar_plantel(sel_inglesa, "plantel_inglaterra.txt")

# Inicio del mundial:
print("BIENVENIDO AL MUNDIAL 2026")
print("-" * 25)

# Menú principal:
while True:
    print("\nMENÚ PRINCIPAL")
    print("-" * 25)
    print("1. Completar planteles")
    print("2. Simular partidos")
    print("3. Salir")

    opcion = input("Selecciona una opción [1, 2 o 3]: ")

    # Cierre del bucle pricipal:
    if opcion == "3":
        print("\nMUNDIAL FINALIZADO\n")
        break
    # Opción de completar planteles:
    elif opcion == "1":
        while True:
            print("\nSelecciones disponibles: \n- Argentina [A]\n- España [E]\n- Francia [F]\n- Inglaterra [I]")
            selecionar_seleccion = input("Selecciona una selección [A, E, F o I]: ").strip().upper()

            if selecionar_seleccion == "A":
                equipo = sel_argentina
                break
            elif selecionar_seleccion == "E":
                equipo = sel_española
                break
            elif selecionar_seleccion == "F":
                equipo = sel_francesa
                break
            elif selecionar_seleccion == "I":
                equipo = sel_inglesa
                break
            else:
                print("\nOPCIÓN INCORRECTA\n")


    # Bucle de completar planteles: 
        while True:
            print(f"\n - SELECCIÓN DE {equipo.nacionalidad.upper()} -")
            print("\nMenú: Selecciones")
            print("-" * 25)
            print("1. Mostrar plantel")
            print("2. Convocar jugador")
            print("3. Quitar jugador")
            print("4. Volver al menú principal")

            opcion_seleccion = input("Seleccioná una opción [1, 2, 3 o 4]: ")
            # Cierre del bucle completar planteles:
            if opcion_seleccion == "4":
                print(f"GESTIÓN DE {equipo.nacionalidad.upper()} FINALIZADA")
                break
            # Mostrar plantel actual:
            elif opcion_seleccion == "1":
                print("\nPLANTEL ACTUAL:")
                print("-" * 25)
                equipo.mostrar_plantel()
            # Convocar jugadores:
            elif opcion_seleccion == "2":
                cantidad = int(input("\n¿Cuántos jugadores vas a convocar? [Ingresa 0 para cancelar] "))
                
                for i in range(cantidad):
                    print(f"\nJugador {i+1}:")
                    nombre = input("Nombre: ").strip().capitalize()
                    apellido = input("Apellido: ").strip().capitalize()
                    posicion = input("Posición: ").strip().capitalize()
                    numero = input("Número: ").strip()

                    jugador_nuevo = Jugador(nombre, apellido, posicion, numero)
                    equipo.convocar(jugador_nuevo)
                
                    datos_jugador = f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion},{jugador_nuevo.numero}\n"
                    escribir_archivo(f"plantel_{equipo.nacionalidad}.txt".lower(), datos_jugador)
                    print(f"\nEl jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} fue seleccionado\n")
            # Quitar jugadores:
            elif opcion_seleccion == "3":
                cantidad_quitar = int(input("\n¿Cuantos jugadores vas a quitar? [Ingresa 0 para cancelar] "))

                for i in range(cantidad_quitar):
                    print(f"\nJugador {i+1} a quitar:")
                    numero_eliminado = input("Ingresa la dorsal del jugador a quitar: ").strip()

                    lineas = leer_archivo(f"plantel_{equipo.nacionalidad}.txt".lower())
                    lineas_nuevas = []

                    for linea in lineas:
                        datos = linea.strip().split(",")
                        if len(datos) == 4 and datos[3] != numero_eliminado:
                            lineas_nuevas.append(linea)

                    # Reescribimos el archivo .txt con los jugadores restantes:
                    reescribir_archivo(f"plantel_{equipo.nacionalidad}.txt".lower(), lineas_nuevas)

                    # Recargamos la selección en memoria desde el archivo actualizado:
                    cargar_plantel(equipo, f"plantel_{equipo.nacionalidad}.txt".lower())

                    print(f"\nEl jugador con la dorsal {numero_eliminado} se quitó de la lista\n")

            else:
                print("\nOPCIÓN INCORRECTA\n")

    # Opción de simular partidos:
    elif opcion == "2":
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