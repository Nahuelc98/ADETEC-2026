import customtkinter as ctk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

# Listas predefinidas para los menús desplegables
CONFEDERACIONES_FIFA = ["CONMEBOL", "UEFA", "CONCACAF", "CAF", "AFC", "OFC"]
POSICIONES_JUGADOR = ["Arquero", "Defensor", "Mediocampista", "Delantero"]


# --- VENTANA 1: GESTIÓN DE SELECCIONES ---
class VentanaGestion(ctk.CTkToplevel):
    def __init__(self, parent, fn_obtener, fn_agregar, fn_eliminar):
        super().__init__(parent)
        self.title("Gestión de Selecciones")
        self.geometry("450x570")
        self.after(100, self.lift)

        self.fn_obtener = fn_obtener
        self.fn_agregar = fn_agregar
        self.fn_eliminar = fn_eliminar

        ctk.CTkLabel(self, text="Gestión de Selecciones", font=("Arial", 20, "bold")).pack(pady=10)

        # Entradas y Menú desplegable para Confederaciones
        self.ent_nombre = ctk.CTkEntry(self, placeholder_text="Nombre (ej: Argentina)", width=280)
        self.ent_nombre.pack(pady=3)

        ctk.CTkLabel(self, text="Confederación:", font=("Arial", 12)).pack(pady=(5, 0))
        self.combo_conf = ctk.CTkOptionMenu(self, values=CONFEDERACIONES_FIFA, width=280)
        self.combo_conf.pack(pady=3)

        self.ent_dt = ctk.CTkEntry(self, placeholder_text="Director Técnico", width=280)
        self.ent_dt.pack(pady=3)

        self.ent_mundiales = ctk.CTkEntry(self, placeholder_text="Mundiales Ganados", width=280)
        self.ent_mundiales.pack(pady=3)

        # Botones
        self.btn_add = ctk.CTkButton(self, text="Agregar / Actualizar Selección", command=self.agregar, width=280)
        self.btn_add.pack(pady=5)

        self.btn_del = ctk.CTkButton(self, text="Eliminar Selección (por nombre)", command=self.eliminar, width=280, fg_color="#D35400", hover_color="#E67E22")
        self.btn_del.pack(pady=5)

        self.btn_list = ctk.CTkButton(self, text="Ver Lista de Selecciones", command=self.listar, width=280)
        self.btn_list.pack(pady=5)

        # Salida
        self.txt_salida = ctk.CTkTextbox(self, width=400, height=160)
        self.txt_salida.pack(pady=10)

    def agregar(self):
        nom = self.ent_nombre.get().strip().capitalize()
        conf = self.combo_conf.get()
        dt = self.ent_dt.get().strip().title()
        mun = self.ent_mundiales.get().strip()

        if nom and conf and dt and mun.isdigit():
            self.fn_agregar(nom, conf, dt, int(mun))
            self.txt_salida.delete("1.0", "end")
            self.txt_salida.insert("end", f"✔ Selección '{nom}' guardada correctamente.\n")
            self.listar()
        else:
            self.txt_salida.delete("1.0", "end")
            self.txt_salida.insert("end", "⚠ Error: Completa el nombre, DT y mundiales (número).")

    def eliminar(self):
        nom = self.ent_nombre.get().strip().capitalize()
        if nom:
            self.fn_eliminar(nom)
            self.txt_salida.delete("1.0", "end")
            self.txt_salida.insert("end", f"✔ Selección '{nom}' eliminada.\n")
            self.listar()

    def listar(self):
        self.txt_salida.delete("1.0", "end")
        datos = self.fn_obtener()
        if not datos:
            self.txt_salida.insert("end", "No hay selecciones en la BD.")
            return
        for s in datos:
            self.txt_salida.insert("end", f"• {s[0].upper()} ({s[1]}) - DT: {s[2]} | Mundiales: {s[3]}\n")


# --- VENTANA 2: COMPLETAR PLANTELES ---
class VentanaPlanteles(ctk.CTkToplevel):
    def __init__(self, parent, fn_nombres, fn_plantel, fn_add_j, fn_del_j):
        super().__init__(parent)
        self.title("Completar Planteles")
        self.geometry("450x620")
        self.after(100, self.lift)

        self.fn_nombres = fn_nombres
        self.fn_plantel = fn_plantel
        self.fn_add_j = fn_add_j
        self.fn_del_j = fn_del_j

        ctk.CTkLabel(self, text="Gestión de Planteles", font=("Arial", 20, "bold")).pack(pady=10)

        # Selección de Equipo
        equipos = self.fn_nombres()
        if not equipos:
            equipos = ["Sin Selecciones"]

        ctk.CTkLabel(self, text="Seleccionar Selección:", font=("Arial", 12)).pack(pady=(2, 0))
        self.combo_equipo = ctk.CTkOptionMenu(self, values=equipos, width=280)
        self.combo_equipo.pack(pady=3)

        # Campos Jugador
        self.ent_nom = ctk.CTkEntry(self, placeholder_text="Nombre Jugador", width=280)
        self.ent_nom.pack(pady=3)
        self.ent_ape = ctk.CTkEntry(self, placeholder_text="Apellido Jugador", width=280)
        self.ent_ape.pack(pady=3)

        ctk.CTkLabel(self, text="Posición:", font=("Arial", 12)).pack(pady=(5, 0))
        self.combo_pos = ctk.CTkOptionMenu(self, values=POSICIONES_JUGADOR, width=280)
        self.combo_pos.pack(pady=3)

        self.ent_dor = ctk.CTkEntry(self, placeholder_text="Dorsal (Número)", width=280)
        self.ent_dor.pack(pady=3)

        # Botones
        self.btn_add = ctk.CTkButton(self, text="Convocar Jugador", command=self.convocar, width=280)
        self.btn_add.pack(pady=5)

        self.btn_del = ctk.CTkButton(self, text="Quitar Jugador (por Dorsal)", command=self.quitar, width=280, fg_color="#D35400", hover_color="#E67E22")
        self.btn_del.pack(pady=5)

        self.btn_ver = ctk.CTkButton(self, text="Mostrar Equipo", command=self.ver_equipo, width=280)
        self.btn_ver.pack(pady=5)

        self.txt_salida = ctk.CTkTextbox(self, width=400, height=150)
        self.txt_salida.pack(pady=10)

    def convocar(self):
        eq = self.combo_equipo.get()
        n = self.ent_nom.get().strip().capitalize()
        a = self.ent_ape.get().strip().capitalize()
        p = self.combo_pos.get()
        d = self.ent_dor.get().strip()

        if n and a and p and d.isdigit():
            self.fn_add_j(n, a, p, int(d), eq)
            self.ver_equipo()

    def quitar(self):
        eq = self.combo_equipo.get()
        d = self.ent_dor.get().strip()
        if d.isdigit():
            self.fn_del_j(eq, int(d))
            self.ver_equipo()

    def ver_equipo(self):
        eq = self.combo_equipo.get()
        self.txt_salida.delete("1.0", "end")
        jugadores = self.fn_plantel(eq)
        self.txt_salida.insert("end", f"=== PLANTEL DE {eq.upper()} ===\n\n")
        if not jugadores:
            self.txt_salida.insert("end", "Sin jugadores convocados.")
            return
        for j in jugadores:
            self.txt_salida.insert("end", f"#{j[2]} - {j[0]} {j[1]} ({j[3]})\n")


# --- VENTANA 3: SIMULACIÓN DE PARTIDOS ---
class VentanaSimulacion(ctk.CTkToplevel):
    def __init__(self, parent, fn_simular):
        super().__init__(parent)
        self.title("Simulador de Partidos")
        self.geometry("500x500")
        self.after(100, self.lift)

        self.fn_simular = fn_simular

        ctk.CTkLabel(self, text="SIMULACIÓN DEL MUNDIAL", font=("Arial", 20, "bold")).pack(pady=10)

        self.btn_iniciar = ctk.CTkButton(
            self, text="▶ Iniciar Torneo", command=self.simular, 
            width=280, height=40, font=("Arial", 16, "bold"),
            fg_color="#27AE60", hover_color="#2ECC71"
        )
        self.btn_iniciar.pack(pady=10)

        self.txt_res = ctk.CTkTextbox(self, width=450, height=360, font=("Consolas", 12))
        self.txt_res.pack(pady=10)

    def simular(self):
        self.txt_res.delete("1.0", "end")
        lineas = self.fn_simular()
        for l in lineas:
            self.txt_res.insert("end", l + "\n")


# --- MENÚ PRINCIPAL ---
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mundial FIFA 2026")
        self.geometry("400x500")

        self.label = ctk.CTkLabel(self, text="MUNDIAL FIFA 2026", font=("Arial", 28, "bold"))
        self.label.pack(padx=20, pady=40)

        self.btn_gestion = ctk.CTkButton(self, text="Gestionar Selecciones", command=self.abrir_gestion, width=250, height=45, font=("Arial", 16, "bold"))
        self.btn_gestion.pack(padx=20, pady=10)

        self.btn_planteles = ctk.CTkButton(self, text="Completar Planteles", command=self.abrir_planteles, width=250, height=45, font=("Arial", 16, "bold"))
        self.btn_planteles.pack(padx=20, pady=10)

        self.btn_simular = ctk.CTkButton(self, text="Simular Partidos", command=self.abrir_simulacion, width=250, height=45, font=("Arial", 16, "bold"))
        self.btn_simular.pack(padx=20, pady=10)

        self.btn_salir = ctk.CTkButton(self, text="Salir", command=self.salir, width=250, height=45, font=("Arial", 16, "bold"), fg_color="#C0392B", hover_color="#E74C3C")
        self.btn_salir.pack(padx=20, pady=10)

    def abrir_gestion(self):
        pass

    def abrir_planteles(self):
        pass

    def abrir_simulacion(self):
        pass

    def salir(self):
        self.destroy()