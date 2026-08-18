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

sel_argentina = SeleccionFutbol("Argentina","Lionel Scaloni",3,"H")

# Cargar el plantel guardado previamente al arrancar el programa:
cargar_plantel(sel_argentina, "plantel_argentina.txt")

print("SELECCIÓN ARGENTINA")
print("-" * 25)

while True:
    print("\nMENU")
    print("-" * 25)
    print("1. Mostrar plantel")
    print("2. Convocar jugador")
    print("3. Quitar jugador")
    print("4. Salir")

    opcion = input("Seleccioná una opción: ")

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
    
       