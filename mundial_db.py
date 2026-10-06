import mysql.connector
import customtkinter as ctk

# Conectar a la base de datos
def conectar(ip, usuario, puerto, contraseña):
    connection = mysql.connector.connect(
        host=ip,
        user=usuario,
        password=contraseña,
        port=puerto,
        database='mundial_db' 
    )
    print("Conectado a la Base de Datos!\n--------------------------------")
    return connection

# Interfaz para ingresar la contraseña de MySQL
def pedir_conexion(ip='127.0.0.1', usuario='root', puerto=3306):
    conexion_activa = None

    class VentanaLogin(ctk.CTk):
        def __init__(self):
            super().__init__()
            self.title("Acceso BD")
            self.geometry("300x200")
            ctk.set_appearance_mode("Dark")
            ctk.set_default_color_theme("green")

            self.label = ctk.CTkLabel(self, text="Conectar a Base de Datos", font=("Arial", 18, "bold"))
            self.label.pack(pady=20)

            self.entry_pass = ctk.CTkEntry(self, placeholder_text="Contraseña de MySQL", show="*", width=220)
            self.entry_pass.pack(pady=5)

            self.lbl_error = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 12))
            self.lbl_error.pack(pady=5)

            self.btn_ingresar = ctk.CTkButton(
                self, text="Ingresar", command=self.validar, 
                width=150, height=40, font=("Arial", 16, "bold")
            )
            self.btn_ingresar.pack(pady=5)

        def validar(self):
            nonlocal conexion_activa
            pwd = self.entry_pass.get()
            try:
                conexion_activa = conectar(ip, usuario, puerto, pwd)
                self.destroy()
            except Exception:
                self.lbl_error.configure(text="Contraseña incorrecta")

    app_login = VentanaLogin()
    app_login.mainloop()
    
    return conexion_activa            

# --- OPERACIONES EN BASE DE DATOS ---

def agregar_seleccion_db(conexion_db, seleccion, confederacion, tecnico, mundiales):
    cursor = conexion_db.cursor()
    sql = """INSERT INTO selecciones (seleccion, confederacion, tecnico, mundiales)
             VALUES (%s, %s, %s, %s);"""
    cursor.execute(sql, (seleccion, confederacion, tecnico, mundiales))
    conexion_db.commit()
    cursor.close()

def eliminar_seleccion_db(conexion_db, seleccion):
    cursor = conexion_db.cursor()
    sql = "DELETE FROM selecciones WHERE seleccion = %s;"
    cursor.execute(sql, (seleccion,))
    conexion_db.commit()
    cursor.close()

def mostrar_selecciones(conexion_db):
    cursor = conexion_db.cursor()
    sql = "SELECT seleccion, confederacion, tecnico, mundiales FROM selecciones;" 
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close() 
    return resultado

def nombres_selecciones(conexion_db):
    cursor = conexion_db.cursor()
    cursor.execute("SELECT seleccion FROM selecciones;")
    resultado = cursor.fetchall()
    cursor.close()
    return [fila[0] for fila in resultado]

def agregar_jugador_db(conexion_db, nombre, apellido, posicion, dorsal, equipo):
    cursor = conexion_db.cursor()
    sql = """INSERT INTO jugadores (nombre, apellido, posicion, dorsal, seleccion)
             VALUES (%s, %s, %s, %s, %s);"""
    cursor.execute(sql, (nombre, apellido, posicion, dorsal, equipo))
    conexion_db.commit()
    cursor.close()

def sacar_jugador_db(conexion_db, equipo, dorsal):
    cursor = conexion_db.cursor()
    sql = "DELETE FROM jugadores WHERE seleccion = %s AND dorsal = %s;"
    cursor.execute(sql, (equipo, dorsal))
    conexion_db.commit()
    cursor.close() 

def mostrar_plantel(conexion_db, equipo):
    cursor = conexion_db.cursor()
    sql = """SELECT nombre, apellido, dorsal, posicion 
              FROM jugadores 
              WHERE seleccion = %s 
              ORDER BY posicion;"""
    cursor.execute(sql, (equipo,))
    resultado = cursor.fetchall()
    cursor.close()
    return resultado

# Conectamos localmente:
#conexion = conectar('127.0.0.1', 'root', 3306)

# Agregamos una selección:
#nueva_seleccion = agregar_seleccion(conexion)

# Eliminamos una selección:
#quitar_seleccion = eliminar_seleccion(conexion)

# Lista de selecciones:
#lista_selecciones = mostrar_selecciones(conexion)

# Nombre de selecciones para simular partidos:
#nombre_selecciones = nombres_selecciones(conexion)
#print(nombre_selecciones)

# Agregamos un jugador:
#nueva_jugador = agregar_jugador(conexion)

# Sacamos un jugador:
#quitar_jugador = sacar_jugador(conexion)

# Mostrar plantel de una selección:
#ver_plantel = mostrar_plantel(conexion)

# Cerramos la conexión total al finalizar:
#conexion.close()