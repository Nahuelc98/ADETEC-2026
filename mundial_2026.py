from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador

# FUNCIÓN ESCRIBIR EN ARCHIVO:
def escribir_archivo(nombre_archivo, texto):
    archivo = open(nombre_archivo, "a", encoding="utf-8")
    archivo.write(texto)
    archivo.close()

# FUNCIÓN LEER ARCHIVO:
def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r", encoding="utf-8")
    contenido = archivo.readlines()
    archivo.close()
    return contenido

sel_argentina = SeleccionFutbol("Argentina", "Lionel Scaloni", 3, "H")

print("SELECCIÓN ARGENTINA")
print("-" * 25 + "\n")

while True:
    print("Seleccioná una opción")
    print("-" * 25)
    print("1. Mostrar plantel")
    print("2. Convocar jugador")
    print("3. Quitar jugador")
    print("4. Salir")

    opcion = input("Ingresa una opción: ")

    if opcion == "4":
        print("SELECCIÓN FINALIZADA")
        break

    elif opcion == "1":
        lineas = leer_archivo("plantel_argentina.txt")
        print("\nPLANTEL GUARDADO")
        for linea in lineas:
            print(linea.strip())

    elif opcion == "2":
        cantidad = int(input("¿Cuántos jugadores vas a convocar? "))
        
        for i in range(cantidad):
            print(f"\nJugador {i+1}:")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            posicion = input("Posición: ")

            jugador_nuevo = Jugador(nombre, apellido, posicion)
            sel_argentina.convocar(jugador_nuevo)

            datos_jugador = f"{jugador_nuevo.nombre},{jugador_nuevo.apellido},{jugador_nuevo.posicion}\n"
            
            escribir_archivo("plantel_argentina.txt", datos_jugador)
            print("Jugador guardado")

    elif opcion == "3":
        print("Ingresa Nombre y Apellido del jugador a sacar del plantel")
        print("-" * 25)
        nombre_eliminado = input("Nombre del jugador: ")
        apellido_eliminado = input("Apellido del jugador: ")

        if nombre_eliminado == jugador_nuevo.nombre and apellido_eliminado == jugador_nuevo.apellido:
            