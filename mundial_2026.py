from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador

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

sel_argentina = SeleccionFutbol("Argentina","Lionel Scaloni",3,"A")
sel_española = SeleccionFutbol("España","Luis de la Fuente",2,"A")
sel_francesa = SeleccionFutbol("Francia","Zinédine Zidane",2,"A")
sel_inglesa = SeleccionFutbol("Inglaterra","Thomas Tuchel",1,"A")

# Cargar el plantel guardado previamente al arrancar el programa:
cargar_plantel(sel_argentina, "plantel_argentina.txt")
cargar_plantel(sel_española, "plantel_españa.txt")
cargar_plantel(sel_francesa, "plantel_francia.txt")
cargar_plantel(sel_inglesa, "plantel_inglaterra.txt")

print("BIENVENIDO AL MUNDIAL 2026")
print("-" * 25)

while True:
    print("\nMENÚ PRINCIPAL")
    print("-" * 25)
    print("1. Completar planteles")
    print("2. Simular partidos")
    print("3. Salir")

    opcion_mundial = input("Selecciona una opción [1, 2 o 3]: ")

    if opcion_mundial == "3":
        print("MUNDIAL CERRADO")
        break

    elif opcion_mundial == "1":
        print("\nSelecciones disponibles: \n- Argentina [A]\n- España [E]\n- Francia [F]\n- Inglaterra [I]")
        selecionar_seleccion = input("Selecciona una selección [A, E, F o I]: ").upper()

        if selecionar_seleccion == "A":
            while True:
                print("\nSELECCIÓN ARGENTINA")
                print("\nMENÚ")
                print("-" * 25)
                print("1. Mostrar plantel")
                print("2. Convocar jugador")
                print("3. Quitar jugador")
                print("4. Volver al menú principal")

                opcion = input("Seleccioná una opción [1, 2, 3 o 4]: ")

                if opcion == "4":
                    print("SELECCIÓN FINALIZADA")
                    break

                elif opcion == "1":
                    print("\nPLANTEL ACTUAL:")
                    print("-" * 25)
                    sel_argentina.mostrar_plantel()
                
                elif opcion == "2":
                    cantidad = int(input("¿Cuántos jugadores vas a convocar? "))
                    
                    for i in range(cantidad):
                        print(f"\nJugador {i+1}:")
                        nombre = input("Nombre: ").strip().capitalize()
                        apellido = input("Apellido: ").strip().capitalize()
                        posicion = input("Posición: ").strip().capitalize()
                        numero = input("Número: ").strip()

                        jugador_nuevo = Jugador(nombre, apellido, posicion, numero)
                        sel_argentina.convocar(jugador_nuevo)
                    
                        datos_jugador = f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion},{jugador_nuevo.numero}\n"
                        escribir_archivo("plantel_argentina.txt", datos_jugador)
                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} fue seleccionado\n")

                elif opcion == "3":
                    cantidad_quitar = int(input("¿Cuantos jugadores vas a quitar? "))

                    for i in range(cantidad_quitar):
                        print(f"\nJugador {i+1} a quitar:")
                        numero_eliminado = input("Ingresa el número del jugador a quitar: ").strip()

                        lineas = leer_archivo("plantel_argentina.txt")
                        lineas_nuevas = []

                        for linea in lineas:
                            datos = linea.strip().split(",")
                            if len(datos) == 4 and datos[3] != numero_eliminado:
                                lineas_nuevas.append(linea)

                        # Reescribimos el archivo .txt con los jugadores restantes:
                        reescribir_archivo("plantel_argentina.txt", lineas_nuevas)

                        # Recargamos la selección en memoria desde el archivo actualizado:
                        cargar_plantel(sel_argentina, "plantel_argentina.txt")

                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} se quitó de la lista\n")

                else:
                    print("\nOPCIÓN INCORRECTA\n")

        elif selecionar_seleccion == "E":
            while True:
                print("\nSELECCIÓN ESPAÑOLA")
                print("\nMENÚ")
                print("-" * 25)
                print("1. Mostrar plantel")
                print("2. Convocar jugador")
                print("3. Quitar jugador")
                print("4. Volver al menú principal")

                opcion = input("Seleccioná una opción [1, 2, 3 o 4]: ")

                if opcion == "4":
                    print("SELECCIÓN FINALIZADA")
                    break

                elif opcion == "1":
                    print("\nPLANTEL ACTUAL:")
                    print("-" * 25)
                    sel_española.mostrar_plantel()
                
                elif opcion == "2":
                    cantidad = int(input("¿Cuántos jugadores vas a convocar? "))
                    
                    for i in range(cantidad):
                        print(f"\nJugador {i+1}:")
                        nombre = input("Nombre: ").strip().capitalize()
                        apellido = input("Apellido: ").strip().capitalize()
                        posicion = input("Posición: ").strip().capitalize()
                        numero = input("Número: ").strip()

                        jugador_nuevo = Jugador(nombre, apellido, posicion, numero)
                        sel_española.convocar(jugador_nuevo)
                    
                        datos_jugador = f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion},{jugador_nuevo.numero}\n"
                        escribir_archivo("plantel_españa.txt", datos_jugador)
                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} fue seleccionado\n")

                elif opcion == "3":
                    cantidad_quitar = int(input("¿Cuantos jugadores vas a quitar? "))

                    for i in range(cantidad_quitar):
                        print(f"\nJugador {i+1} a quitar:")
                        numero_eliminado = input("Ingresa el número del jugador a quitar: ").strip()

                        lineas = leer_archivo("plantel_españa.txt")
                        lineas_nuevas = []

                        for linea in lineas:
                            datos = linea.strip().split(",")
                            if len(datos) == 4 and datos[3] != numero_eliminado:
                                lineas_nuevas.append(linea)

                        # Reescribimos el archivo .txt con los jugadores restantes:
                        reescribir_archivo("plantel_españa.txt", lineas_nuevas)

                        # Recargamos la selección en memoria desde el archivo actualizado:
                        cargar_plantel(sel_española, "plantel_españa.txt")

                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} se quitó de la lista\n")

                else:
                    print("\nOPCIÓN INCORRECTA\n")        

        elif selecionar_seleccion == "F":
            while True:
                print("\nSELECCIÓN FRANCESA")
                print("\nMENÚ")
                print("-" * 25)
                print("1. Mostrar plantel")
                print("2. Convocar jugador")
                print("3. Quitar jugador")
                print("4. Volver al menú principal")

                opcion = input("Seleccioná una opción [1, 2, 3 o 4]: ")

                if opcion == "4":
                    print("SELECCIÓN FINALIZADA")
                    break

                elif opcion == "1":
                    print("\nPLANTEL ACTUAL:")
                    print("-" * 25)
                    sel_francesa.mostrar_plantel()
                
                elif opcion == "2":
                    cantidad = int(input("¿Cuántos jugadores vas a convocar? "))
                    
                    for i in range(cantidad):
                        print(f"\nJugador {i+1}:")
                        nombre = input("Nombre: ").strip().capitalize()
                        apellido = input("Apellido: ").strip().capitalize()
                        posicion = input("Posición: ").strip().capitalize()
                        numero = input("Número: ").strip()

                        jugador_nuevo = Jugador(nombre, apellido, posicion, numero)
                        sel_francesa.convocar(jugador_nuevo)
                    
                        datos_jugador = f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion},{jugador_nuevo.numero}\n"
                        escribir_archivo("plantel_francia.txt", datos_jugador)
                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} fue seleccionado\n")

                elif opcion == "3":
                    cantidad_quitar = int(input("¿Cuantos jugadores vas a quitar? "))

                    for i in range(cantidad_quitar):
                        print(f"\nJugador {i+1} a quitar:")
                        numero_eliminado = input("Ingresa el número del jugador a quitar: ").strip()

                        lineas = leer_archivo("plantel_francia.txt")
                        lineas_nuevas = []

                        for linea in lineas:
                            datos = linea.strip().split(",")
                            if len(datos) == 4 and datos[3] != numero_eliminado:
                                lineas_nuevas.append(linea)

                        # Reescribimos el archivo .txt con los jugadores restantes:
                        reescribir_archivo("plantel_francia.txt", lineas_nuevas)

                        # Recargamos la selección en memoria desde el archivo actualizado:
                        cargar_plantel(sel_francesa, "plantel_francia.txt")

                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} se quitó de la lista\n")

                else:
                    print("\nOPCIÓN INCORRECTA\n") 

        elif selecionar_seleccion == "I":
            while True:
                print("\nSELECCIÓN INGLESA")
                print("\nMENÚ")
                print("-" * 25)
                print("1. Mostrar plantel")
                print("2. Convocar jugador")
                print("3. Quitar jugador")
                print("4. Volver al menú principal")

                opcion = input("Seleccioná una opción [1, 2, 3 o 4]: ")

                if opcion == "4":
                    print("SELECCIÓN FINALIZADA")
                    break

                elif opcion == "1":
                    print("\nPLANTEL ACTUAL:")
                    print("-" * 25)
                    sel_inglesa.mostrar_plantel()
                
                elif opcion == "2":
                    cantidad = int(input("¿Cuántos jugadores vas a convocar? "))
                    
                    for i in range(cantidad):
                        print(f"\nJugador {i+1}:")
                        nombre = input("Nombre: ").strip().capitalize()
                        apellido = input("Apellido: ").strip().capitalize()
                        posicion = input("Posición: ").strip().capitalize()
                        numero = input("Número: ").strip()

                        jugador_nuevo = Jugador(nombre, apellido, posicion, numero)
                        sel_inglesa.convocar(jugador_nuevo)
                    
                        datos_jugador = f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion},{jugador_nuevo.numero}\n"
                        escribir_archivo("plantel_inglaterra.txt", datos_jugador)
                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} fue seleccionado\n")

                elif opcion == "3":
                    cantidad_quitar = int(input("¿Cuantos jugadores vas a quitar? "))

                    for i in range(cantidad_quitar):
                        print(f"\nJugador {i+1} a quitar:")
                        numero_eliminado = input("Ingresa el número del jugador a quitar: ").strip()

                        lineas = leer_archivo("plantel_inglaterra.txt")
                        lineas_nuevas = []

                        for linea in lineas:
                            datos = linea.strip().split(",")
                            if len(datos) == 4 and datos[3] != numero_eliminado:
                                lineas_nuevas.append(linea)

                        # Reescribimos el archivo .txt con los jugadores restantes:
                        reescribir_archivo("plantel_inglaterra.txt", lineas_nuevas)

                        # Recargamos la selección en memoria desde el archivo actualizado:
                        cargar_plantel(sel_inglesa, "plantel_inglaterra.txt")

                        print(f"El jugador {jugador_nuevo.nombre} {jugador_nuevo.apellido} se quitó de la lista\n")

                else:
                    print("\nOPCIÓN INCORRECTA\n") 

        else:
            print("\nOPCIÓN INCORRECTA\n")
