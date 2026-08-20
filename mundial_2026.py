from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador
import random

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

    opcion_mundial = input("Selecciona una opción [1, 2 o 3]: ")

    # Cierre del bucle pricipal:
    if opcion_mundial == "3":
        print("MUNDIAL CERRADO")
        break
    # Opción de completar planteles:
    elif opcion_mundial == "1":
        print("\nSelecciones disponibles: \n- Argentina [A]\n- España [E]\n- Francia [F]\n- Inglaterra [I]")
        selecionar_seleccion = input("Selecciona una selección [A, E, F o I]: ").upper()

        if selecionar_seleccion == "A":
            equipo = sel_argentina
        elif selecionar_seleccion == "E":
            equipo = sel_española
        elif selecionar_seleccion == "F":
            equipo = sel_francesa
        elif selecionar_seleccion == "I":
            equipo = sel_inglesa
        else:
            print("\nOPCIÓN INCORRECTA\n")

        # Bucle de completar planteles: 
        while True:
            print(f"\nSelección {equipo.nacionalidad}")
            print("\nMenú")
            print("-" * 25)
            print("1. Mostrar plantel")
            print("2. Convocar jugador")
            print("3. Quitar jugador")
            print("4. Volver al menú principal")

            opcion = input("Seleccioná una opción [1, 2, 3 o 4]: ")
            # Cierre del bucle completar planteles:
            if opcion == "4":
                print("SELECCIÓN FINALIZADA")
                break
            # Mostrar plantel actual:
            elif opcion == "1":
                print("\nPLANTEL ACTUAL:")
                print("-" * 25)
                equipo.mostrar_plantel()
            # Convocar jugadores:
            elif opcion == "2":
                cantidad = int(input("¿Cuántos jugadores vas a convocar? "))
                
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
                    print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} fue seleccionado\n")
            # Quitar jugadores:
            elif opcion == "3":
                cantidad_quitar = int(input("¿Cuantos jugadores vas a quitar? "))

                for i in range(cantidad_quitar):
                    print(f"\nJugador {i+1} a quitar:")
                    numero_eliminado = input("Ingresa el número del jugador a quitar: ").strip()

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

                    print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} se quitó de la lista\n")

            else:
                print("\nOPCIÓN INCORRECTA\n")

    # Opción de simular partidos:
    elif opcion_mundial == "2":
        print("\nSIMULACIÓN DE PARTIDOS")






    else:
        print("\nOPCIÓN INCORRECTA\n")