import mysql.connector
import getpass

# Conectar a la base de datos:
def conectar(ip, usuario, puerto):
    connection = mysql.connector.connect(
        host=ip,
        user=usuario,
        password=getpass.getpass("Ingrese la contraseña: "),
        #password="root",
        port=puerto,
        database='mundial_db' 
    )
    print("Conectado a la Base de Datos!\n--------------------------------")
    return connection

# TABLA SELECCIONES:
# Agregar selección:       
def agregar_seleccion(conexion_db):
    seleccion = input("Ingresa el nombre de la selección: ").strip().capitalize()
    confederacion = input("Ingresa la confederación de la selección: ").strip().upper()
    tecnico = input("Ingresa el nombre del técnico de la selección: ").strip().title()
    mundiales = int(input("Ingresa la cantidad de mundiales de la selección: "))
    cursor = conexion_db.cursor()
    sql = f"""INSERT INTO selecciones (seleccion, confederacion, tecnico, mundiales)
    VALUES ('{seleccion}', '{confederacion}', '{tecnico}', {mundiales});"""
    cursor.execute(sql)
    conexion_db.commit()
    cursor.close()
    print(f"\nLa selección {seleccion.capitalize()} se sumo al mundial!!!")

# Eliminar selección:
def eliminar_seleccion(conexion_db):
    seleccion = input("Ingresa el nombre de la selección que quedo eliminada: ").strip().capitalize()
    cursor = conexion_db.cursor()
    sql = f"DELETE FROM selecciones WHERE seleccion = '{seleccion}';"
    cursor.execute(sql)
    conexion_db.commit()
    cursor.close()
    print(f"Selección de {seleccion}, eliminada del mundial.")

# Mostrar selecciones:
def mostrar_selecciones(conexion_db):
    print("\nLISTA DE SELECCIONES:")
    print("-" * 25)
    cursor = conexion_db.cursor()
    sql = "SELECT seleccion, confederacion, tecnico, mundiales FROM selecciones;" 
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close() 
    for seleccion in resultado:
        print(f"{seleccion[0]} ({seleccion[1]}) - DT: {seleccion[2]} | Mundiales: {seleccion[3]}")
    return resultado

# Agregar jugador:       
def agregar_jugador(conexion_db, equipo):
    nombre = input("\nNombre: ").strip().capitalize()
    apellido = input("Apellido: ").strip().capitalize()
    posicion = input("Posición: ").strip().capitalize()
    dorsal = int(input("Dorsal: "))
    cursor = conexion_db.cursor()
    sql = f"""INSERT INTO jugadores (nombre, apellido, posicion, dorsal, seleccion)
    VALUES ('{nombre}', '{apellido}', '{posicion}', {dorsal}, '{equipo}');"""
    cursor.execute(sql)
    conexion_db.commit()
    cursor.close()
    print(f"Jugador {nombre.capitalize()} {apellido.capitalize()} se sumo al plantel de {equipo}")

# Sacamos un jugador por su dorsal:
def sacar_jugador(conexion_db, equipo):
    dorsal = int(input("Ingresa la dorsal del jugador: "))
    cursor = conexion_db.cursor()
    sql = f"DELETE FROM jugadores WHERE seleccion = '{equipo}' AND dorsal = {dorsal};"
    cursor.execute(sql)
    conexion_db.commit()
    cursor.close() 
    print(f"Jugador #{dorsal} de {equipo}, fue desconvocado.")

# Mostrar plantel:
def mostrar_plantel(conexion_db, equipo):
    print(f"VER PLANTEL DE LA {equipo.upper()}")
    print("-" * 20)
    cursor = conexion_db.cursor()
    sql = f"""SELECT nombre, apellido, dorsal, posicion 
              FROM jugadores 
              WHERE seleccion = '{equipo}' 
              ORDER BY posicion;"""
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    for jugador in resultado:
        print(f"{jugador[3]}: #{jugador[2]} {jugador[0]} {jugador[1]}")
    return resultado

# Conectamos localmente:
conexion = conectar('127.0.0.1', 'root', 3306)

# Agregamos una selección:
#nueva_seleccion = agregar_seleccion(conexion)

# Eliminamos una selección:
#quitar_seleccion = eliminar_seleccion(conexion)

# Lista de selecciones:
#lista_selecciones = mostrar_selecciones(conexion)

# Agregamos un jugador:
#nueva_jugador = agregar_jugador(conexion)

# Sacamos un jugador:
#quitar_jugador = sacar_jugador(conexion)

# Mostrar plantel de una selección:
#ver_plantel = mostrar_plantel(conexion)

# Cerramos la conexión total al finalizar:
conexion.close()