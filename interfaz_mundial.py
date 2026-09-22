import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x500")

        self.button = customtkinter.CTkButton(self, text="COMENZAR MUNDIAL", command=self.button_callbck)
        self.button.pack(padx=20, pady=70)

    def button_callbck(self):
        print("Comenzo el mundial")

app = App()
app.mainloop()

# import random
# import customtkinter as ctk
# from tkinter import messagebox

# # Configuración básica de CustomTkinter
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")


# # ==========================================
# # 1. PANTALLAS SECUNDARIAS DE MODIFICACIÓN
# # ==========================================

# class EditarDatosWindow(ctk.CTkToplevel):
#     """Formulario para editar la información de una selección."""
#     def __init__(self, parent, equipo_nombre, app_data):
#         super().__init__(parent)
#         self.title(f"Editar Datos: {equipo_nombre}")
#         self.geometry("380x320")
#         self.after(100, self.lift)
#         self.app_data = app_data
#         self.equipo_nombre = equipo_nombre
#         datos = self.app_data[equipo_nombre]

#         ctk.CTkLabel(self, text=f"Editar {equipo_nombre}", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

#         self.entry_dt = ctk.CTkEntry(self, placeholder_text="Nombre de DT")
#         self.entry_dt.pack(pady=5, padx=20, fill="x")
#         self.entry_dt.insert(0, datos["dt"])

#         self.entry_titulos = ctk.CTkEntry(self, placeholder_text="Títulos Ganados")
#         self.entry_titulos.pack(pady=5, padx=20, fill="x")
#         self.entry_titulos.insert(0, str(datos["titulos"]))

#         self.entry_grupo = ctk.CTkEntry(self, placeholder_text="Grupo")
#         self.entry_grupo.pack(pady=5, padx=20, fill="x")
#         self.entry_grupo.insert(0, datos["grupo"])

#         ctk.CTkButton(self, text="Guardar Cambios", command=self.guardar).pack(pady=15)

#     def guardar(self):
#         dt = self.entry_dt.get().strip()
#         titulos = self.entry_titulos.get().strip()
#         grupo = self.entry_grupo.get().strip()

#         if not dt or not titulos or not grupo:
#             messagebox.showerror("Error", "Todos los campos son obligatorios.")
#             return

#         self.app_data[self.equipo_nombre]["dt"] = dt
#         self.app_data[self.equipo_nombre]["titulos"] = titulos
#         self.app_data[self.equipo_nombre]["grupo"] = grupo.upper()
#         messagebox.showinfo("Éxito", "Datos actualizados correctamente.")
#         self.destroy()


# class ConvocarJugadorWindow(ctk.CTkToplevel):
#     """Formulario para convocar jugadores a la selección."""
#     def __init__(self, parent, equipo_nombre, app_data):
#         super().__init__(parent)
#         self.title(f"Convocar Jugador - {equipo_nombre}")
#         self.geometry("380x350")
#         self.after(100, self.lift)
#         self.app_data = app_data
#         self.equipo_nombre = equipo_nombre

#         ctk.CTkLabel(self, text=f"Convocar a {equipo_nombre}", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

#         self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
#         self.entry_nombre.pack(pady=5, padx=20, fill="x")

#         self.entry_apellido = ctk.CTkEntry(self, placeholder_text="Apellido")
#         self.entry_apellido.pack(pady=5, padx=20, fill="x")

#         self.combo_posicion = ctk.CTkComboBox(self, values=["Portero", "Defensor", "Mediocampista", "Delantero"])
#         self.combo_posicion.pack(pady=5, padx=20, fill="x")

#         self.entry_dorsal = ctk.CTkEntry(self, placeholder_text="Dorsal (Número)")
#         self.entry_dorsal.pack(pady=5, padx=20, fill="x")

#         ctk.CTkButton(self, text="Convocar", command=self.guardar).pack(pady=15)

#     def guardar(self):
#         nombre = self.entry_nombre.get().strip()
#         apellido = self.entry_apellido.get().strip()
#         posicion = self.combo_posicion.get()
#         dorsal = self.entry_dorsal.get().strip()

#         if not nombre or not apellido or not dorsal:
#             messagebox.showerror("Error", "Todos los campos son obligatorios.")
#             return

#         jugador = {"nombre": nombre, "apellido": apellido, "posicion": posicion, "dorsal": dorsal}
#         self.app_data[self.equipo_nombre]["jugadores"].append(jugador)
#         messagebox.showinfo("Éxito", f"{nombre} {apellido} convocado exitosamente.")
#         self.destroy()


# class MostrarJugadoresWindow(ctk.CTkToplevel):
#     """Lista scrolleable con información de jugadores."""
#     def __init__(self, parent, equipo_nombre, app_data):
#         super().__init__(parent)
#         self.title(f"Jugadores Convocados: {equipo_nombre}")
#         self.geometry("400x350")
#         self.after(100, self.lift)

#         jugadores = app_data[equipo_nombre]["jugadores"]
#         ctk.CTkLabel(self, text=f"Plantel de {equipo_nombre}", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

#         scroll_frame = ctk.CTkScrollableFrame(self, width=350, height=250)
#         scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

#         if not jugadores:
#             ctk.CTkLabel(scroll_frame, text="No hay jugadores convocados.").pack(pady=20)
#         else:
#             for j in jugadores:
#                 info = f"#{j['dorsal']} - {j['nombre']} {j['apellido']} ({j['posicion']})"
#                 ctk.CTkLabel(scroll_frame, text=info, anchor="w").pack(pady=5, padx=10, fill="x")


# class EliminarJugadorWindow(ctk.CTkToplevel):
#     """Lista interactiva para desafectar o retirar un jugador de la plantilla."""
#     def __init__(self, parent, equipo_nombre, app_data):
#         super().__init__(parent)
#         self.title(f"Eliminar Jugadores: {equipo_nombre}")
#         self.geometry("400x350")
#         self.after(100, self.lift)
#         self.app_data = app_data
#         self.equipo_nombre = equipo_nombre

#         ctk.CTkLabel(self, text="Selecciona el jugador a retirar", font=ctk.CTkFont(size=14, weight="bold")).pack(pady=10)

#         self.scroll_frame = ctk.CTkScrollableFrame(self, width=350, height=220)
#         self.scroll_frame.pack(pady=5, padx=10, fill="both", expand=True)

#         self.cargar_jugadores()

#     def cargar_jugadores(self):
#         for widget in self.scroll_frame.winfo_children():
#             widget.destroy()

#         jugadores = self.app_data[self.equipo_nombre]["jugadores"]
#         if not jugadores:
#             ctk.CTkLabel(self.scroll_frame, text="No hay jugadores para eliminar.").pack(pady=20)
#             return

#         for idx, j in enumerate(jugadores):
#             row = ctk.CTkFrame(self.scroll_frame)
#             row.pack(fill="x", pady=2, padx=5)
#             text = f"#{j['dorsal']} {j['nombre']} {j['apellido']}"
#             ctk.CTkLabel(row, text=text).pack(side="left", padx=5)
#             ctk.CTkButton(
#                 row, text="Retirar", fg_color="red", hover_color="#990000", width=60,
#                 command=lambda i=idx: self.eliminar(i)
#             ).pack(side="right", padx=5)

#     def eliminar(self, index):
#         jugador = self.app_data[self.equipo_nombre]["jugadores"].pop(index)
#         messagebox.showinfo("Eliminado", f"Se ha retirado a {jugador['nombre']} {jugador['apellido']}.")
#         self.cargar_jugadores()


# # ==========================================
# # 2. PANTALLAS PRINCIPALES DEL MENÚ
# # ==========================================

# class CrearSeleccionWindow(ctk.CTkToplevel):
#     def __init__(self, parent, app_data):
#         super().__init__(parent)
#         self.title("Crear Selección")
#         self.geometry("380x380")
#         self.after(100, self.lift)
#         self.app_data = app_data

#         ctk.CTkLabel(self, text="Nueva Selección", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=15)

#         self.entry_nac = ctk.CTkEntry(self, placeholder_text="Nacionalidad / País")
#         self.entry_nac.pack(pady=8, padx=20, fill="x")

#         self.entry_dt = ctk.CTkEntry(self, placeholder_text="Nombre de DT")
#         self.entry_dt.pack(pady=8, padx=20, fill="x")

#         self.entry_titulos = ctk.CTkEntry(self, placeholder_text="Títulos Ganados")
#         self.entry_titulos.pack(pady=8, padx=20, fill="x")

#         self.entry_grupo = ctk.CTkEntry(self, placeholder_text="Grupo (Ej: A, B, C...)")
#         self.entry_grupo.pack(pady=8, padx=20, fill="x")

#         ctk.CTkButton(self, text="Guardar Selección", command=self.guardar).pack(pady=15)

#     def guardar(self):
#         nac = self.entry_nac.get().strip()
#         dt = self.entry_dt.get().strip()
#         titulos = self.entry_titulos.get().strip()
#         grupo = self.entry_grupo.get().strip()

#         if not nac or not dt or not titulos or not grupo:
#             messagebox.showerror("Error", "Todos los campos son obligatorios.")
#             return

#         if nac in self.app_data:
#             messagebox.showerror("Error", "Esa selección ya existe.")
#             return

#         self.app_data[nac] = {"dt": dt, "titulos": titulos, "grupo": grupo.upper(), "jugadores": []}
#         messagebox.showinfo("Éxito", f"Selección de {nac} creada.")
#         self.destroy()


# class MostrarSeleccionesWindow(ctk.CTkToplevel):
#     def __init__(self, parent, app_data):
#         super().__init__(parent)
#         self.title("Listado de Selecciones")
#         self.geometry("450x400")
#         self.after(100, self.lift)

#         ctk.CTkLabel(self, text="Selecciones Registradas", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

#         textbox = ctk.CTkTextbox(self, width=400, height=300)
#         textbox.pack(pady=10, padx=10, fill="both", expand=True)

#         if not app_data:
#             textbox.insert("end", "No hay selecciones registradas todavía.")
#         else:
#             for pais, datos in app_data.items():
#                 info = (
#                     f"🏆 SELECCIÓN: {pais.upper()}\n"
#                     f"   • Director Técnico: {datos['dt']}\n"
#                     f"   • Títulos Ganados: {datos['titulos']}\n"
#                     f"   • Grupo: {datos['grupo']}\n"
#                     f"   • Convocados: {len(datos['jugadores'])} jugadores\n"
#                     f"{'-'*40}\n"
#                 )
#                 textbox.insert("end", info)

#         textbox.configure(state="disabled")


# class ModificarSeleccionesWindow(ctk.CTkToplevel):
#     def __init__(self, parent, app_data):
#         super().__init__(parent)
#         self.title("Modificar Selección")
#         self.geometry("400x320")
#         self.after(100, self.lift)
#         self.app_data = app_data

#         ctk.CTkLabel(self, text="Gestión de Selecciones", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

#         equipos = list(self.app_data.keys())
#         if not equipos:
#             ctk.CTkLabel(self, text="No hay selecciones disponibles.").pack(pady=20)
#             return

#         self.combo = ctk.CTkComboBox(self, values=equipos)
#         self.combo.pack(pady=10, padx=20, fill="x")

#         ctk.CTkButton(self, text="Modificar datos de la selección", command=self.modificar_datos).pack(pady=6, padx=20, fill="x")
#         ctk.CTkButton(self, text="Convocar jugadores", command=self.convocar).pack(pady=6, padx=20, fill="x")
#         ctk.CTkButton(self, text="Mostrar jugadores", command=self.mostrar_jugadores).pack(pady=6, padx=20, fill="x")
#         ctk.CTkButton(self, text="Eliminar jugadores", command=self.eliminar_jugadores).pack(pady=6, padx=20, fill="x")

#     def modificar_datos(self):
#         EditarDatosWindow(self, self.combo.get(), self.app_data)

#     def convocar(self):
#         ConvocarJugadorWindow(self, self.combo.get(), self.app_data)

#     def mostrar_jugadores(self):
#         MostrarJugadoresWindow(self, self.combo.get(), self.app_data)

#     def eliminar_jugadores(self):
#         EliminarJugadorWindow(self, self.combo.get(), self.app_data)


# class EliminarSeleccionWindow(ctk.CTkToplevel):
#     def __init__(self, parent, app_data):
#         super().__init__(parent)
#         self.title("Eliminar Selección")
#         self.geometry("380x200")
#         self.after(100, self.lift)
#         self.app_data = app_data

#         ctk.CTkLabel(self, text="Eliminar Selección", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)

#         equipos = list(self.app_data.keys())
#         if not equipos:
#             ctk.CTkLabel(self, text="No hay selecciones disponibles.").pack(pady=20)
#             return

#         self.combo = ctk.CTkComboBox(self, values=equipos)
#         self.combo.pack(pady=10, padx=20, fill="x")

#         ctk.CTkButton(self, text="Eliminar", fg_color="red", hover_color="#990000", command=self.eliminar).pack(pady=15)

#     def eliminar(self):
#         seleccion = self.combo.get()
#         if seleccion in self.app_data:
#             del self.app_data[seleccion]
#             messagebox.showinfo("Eliminada", f"La selección {seleccion} ha sido eliminada.")
#             self.destroy()


# # ==========================================
# # 3. MOTOR Y PANTALLA DE JUGAR PARTIDOS
# # ==========================================

# class JugarPartidosWindow(ctk.CTkToplevel):
#     """Simulador progresivo de fases eliminatorias."""
#     def __init__(self, parent, app_data):
#         super().__init__(parent)
#         self.title("Fase de Partidos - Mundial FIFA 2026")
#         self.geometry("550x550")
#         self.after(100, self.lift)

#         self.app_data = app_data
#         self.fases_nombres = ["Fase de Grupos / Octavos", "Cuartos de Final", "Semifinal", "Final"]
#         self.fase_actual_idx = 0
#         self.partidos_ui = []

#         # Obtener selecciones e iniciar cuadro
#         self.equipos = list(app_data.keys())
#         random.shuffle(self.equipos)

#         if len(self.equipos) < 2:
#             ctk.CTkLabel(self, text="Se necesitan al menos 2 selecciones para jugar.").pack(pady=20)
#             return

#         self.lbl_fase = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=18, weight="bold"))
#         self.lbl_fase.pack(pady=10)

#         self.scroll_partidos = ctk.CTkScrollableFrame(self, width=500, height=350)
#         self.scroll_partidos.pack(pady=10, padx=10, fill="both", expand=True)

#         self.btn_siguiente = ctk.CTkButton(
#             self, text="Pasar a la Siguiente Ronda", state="disabled", command=self.siguiente_ronda
#         )
#         self.btn_siguiente.pack(pady=15)

#         self.armar_cruces()

#     def armar_cruces(self):
#         for widget in self.scroll_partidos.winfo_children():
#             widget.destroy()

#         self.partidos_ui.clear()
#         nombre_fase = self.fases_nombres[min(self.fase_actual_idx, len(self.fases_nombres)-1)]
#         self.lbl_fase.configure(text=f"Etapa: {nombre_fase}")

#         # Emparejamiento por parejas
#         for i in range(0, len(self.equipos) - 1, 2):
#             eq1 = self.equipos[i]
#             eq2 = self.equipos[i+1]

#             frame_p = ctk.CTkFrame(self.scroll_partidos)
#             frame_p.pack(fill="x", pady=5, padx=5)

#             lbl_match = ctk.CTkLabel(frame_p, text=f"{eq1}  vs  {eq2}", font=ctk.CTkFont(weight="bold"))
#             lbl_match.pack(side="left", padx=10)

#             lbl_score = ctk.CTkLabel(frame_p, text=" - vs - ", width=80)
#             lbl_score.pack(side="left", padx=10)

#             btn_sim = ctk.CTkButton(
#                 frame_p, text="Simular", width=80,
#                 command=lambda e1=eq1, e2=eq2, ls=lbl_score, idx=len(self.partidos_ui): self.simular_partido(e1, e2, ls, idx)
#             )
#             btn_sim.pack(side="right", padx=10)

#             self.partidos_ui.append({
#                 "eq1": eq1, "eq2": eq2, "score_label": lbl_score,
#                 "btn": btn_sim, "ganador": None
#             })

#         # Si el número de equipos es impar, pasa uno automáticamente
#         if len(self.equipos) % 2 != 0:
#             pasa_directo = self.equipos[-1]
#             lbl_libre = ctk.CTkLabel(
#                 self.scroll_partidos, text=f"{pasa_directo} avanza automáticamente por libre.",
#                 font=ctk.CTkFont(slant="italic")
#             )
#             lbl_libre.pack(pady=5)
#             self.partidos_ui.append({"ganador": pasa_directo, "bypass": True})

#         self.btn_siguiente.configure(state="disabled")

#     def simular_partido(self, eq1, eq2, lbl_score, idx):
#         goles1 = random.randint(0, 5)
#         goles2 = random.randint(0, 5)

#         # En caso de empate en fase de eliminación, definir por penales aleatorios
#         if goles1 == goles2:
#             if random.choice([True, False]):
#                 goles1 += 1
#             else:
#                 goles2 += 1

#         lbl_score.configure(text=f"{goles1} - {goles2}")
#         ganador = eq1 if goles1 > goles2 else eq2
#         self.partidos_ui[idx]["ganador"] = ganador
#         self.partidos_ui[idx]["btn"].configure(state="disabled")

#         # Verificar si todos los partidos de la ronda finalizaron
#         if all(p["ganador"] is not None for p in self.partidos_ui):
#             self.btn_siguiente.configure(state="normal")

#     def siguiente_ronda(self):
#         ganadores = [p["ganador"] for p in self.partidos_ui]

#         if len(ganadores) == 1:
#             # ¡Hay Campeón!
#             campeon = ganadores[0]
#             messagebox.showinfo("🏆 CAMPEÓN DEL MUNDIAL", f"¡¡ {campeon.upper()} ES EL CAMPEÓN DEL MUNDIAL FIFA 2026 !! 🏆🎉")
#             self.destroy()
#             return

#         self.equipos = ganadores
#         self.fase_actual_idx += 1
#         self.armar_cruces()


# # ==========================================
# # 4. PANTALLA PRINCIPAL (MAIN APP)
# # ==========================================

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Mundial FIFA 2026")
#         self.geometry("450x500")

#         # Base de datos local precargada con datos de ejemplo
#         self.teams_data = {
#             "Argentina": {"dt": "Lionel Scaloni", "titulos": "3", "grupo": "A", "jugadores": [
#                 {"nombre": "Lionel", "apellido": "Messi", "posicion": "Delantero", "dorsal": "10"}
#             ]},
#             "Brasil": {"dt": "Dorival Júnior", "titulos": "5", "grupo": "A", "jugadores": []},
#             "España": {"dt": "Luis de la Fuente", "titulos": "1", "grupo": "B", "jugadores": []},
#             "Francia": {"dt": "Didier Deschamps", "titulos": "2", "grupo": "B", "jugadores": []}
#         }

#         # Encabezado
#         self.title_label = ctk.CTkLabel(
#             self, text="Mundial FIFA 2026", font=ctk.CTkFont(size=24, weight="bold")
#         )
#         self.title_label.pack(pady=25)

#         # Botones del Menú Principal
#         ctk.CTkButton(
#             self, text="Crear selección de fútbol", width=250, height=35,
#             command=self.open_crear
#         ).pack(pady=8)

#         ctk.CTkButton(
#             self, text="Mostrar selecciones", width=250, height=35,
#             command=self.open_mostrar
#         ).pack(pady=8)

#         ctk.CTkButton(
#             self, text="Modificar selecciones", width=250, height=35,
#             command=self.open_modificar
#         ).pack(pady=8)

#         ctk.CTkButton(
#             self, text="Eliminar selecciones", width=250, height=35,
#             command=self.open_eliminar
#         ).pack(pady=8)

#         # Botón Prominente "Jugar partidos"
#         self.btn_jugar = ctk.CTkButton(
#             self, 
#             text="⚽ JUGAR PARTIDOS", 
#             width=280, 
#             height=55, 
#             fg_color="#28a745", 
#             hover_color="#1e7e34",
#             font=ctk.CTkFont(size=18, weight="bold"),
#             command=self.open_jugar
#         )
#         self.btn_jugar.pack(pady=(25, 10))

#     # Handlers para abrir las ventanas
#     def open_crear(self):
#         CrearSeleccionWindow(self, self.teams_data)

#     def open_mostrar(self):
#         MostrarSeleccionesWindow(self, self.teams_data)

#     def open_modificar(self):
#         ModificarSeleccionesWindow(self, self.teams_data)

#     def open_eliminar(self):
#         EliminarSeleccionWindow(self, self.teams_data)

#     def open_jugar(self):
#         JugarPartidosWindow(self, self.teams_data)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()