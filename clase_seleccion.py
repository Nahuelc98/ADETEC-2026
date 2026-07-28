#Generar la clase Seleccion de futbol
class SeleccionFutbol:
    """Clase para las selecciones de fútbol"""
    def __init__(self, nacionalidad, dt,titulos,grupo):
        self.nacionalidad = nacionalidad
        self.director_tecnico = dt
        self.titulos = titulos
        self.convocados = []
        self.puntos=0
        self.grupo=grupo

    def __str__(self):
        return f"Esta es la seleccion de {self.nacionalidad}, dirigida por {self.director_tecnico}"
    
    #Método Convocar
    def convocar(self, jugador):
        "Incorporar un jugador a la plantilla"
        # self.convocados.append({"posicion":jugador.posicion,
        #                         "nombre":jugador.nombre,
        #                         "apellido":jugador.apellido})
        self.convocados.append(jugador)

    #Método Mostrar convocados
    def mostrar_plantel(self):
        # self.convocados.sort(key=lambda x: x["posicion"])

        # print ("Arqueros:")
        # for jugador in self.convocados:
        #     if jugador["posicion"] == "Arquero":
        #         print(f"{jugador["nombre"]} {jugador["apellido"]}")
        # print ("\nDefensores:")
        # for jugador in self.convocados:
        #     if jugador["posicion"] == "Defensor":
        #         print(f"{jugador["nombre"]} {jugador["apellido"]}")
        # print ("\nMediocampistas:")
        # for jugador in self.convocados:
        #     if jugador["posicion"] == "Mediocampista":
        #         print(f"{jugador["nombre"]} {jugador["apellido"]}")
        # print ("\nDelanteros:")
        # for jugador in self.convocados:
        #     if jugador["posicion"] == "Delatero":
        #         print(f"{jugador["nombre"]} {jugador["apellido"]}")
        print ("Arqueros:")
        for jugador in self.convocados:
            if jugador.posicion == "Arquero":
                print(f"{jugador.nombre} {jugador.apellido}")
        print ("\nDefensores:")
        for jugador in self.convocados:
            if jugador.posicion == "Defensor":
                print(f"{jugador.nombre} {jugador.apellido}")
        print ("\nMediocampistas:")
        for jugador in self.convocados:
            if jugador.posicion == "Mediocampista":
                print(f"{jugador.nombre} {jugador.apellido}")
        print ("\nDelanteros:")
        for jugador in self.convocados:
            if jugador.posicion == "Delantero":
                print(f"{jugador.nombre} {jugador.apellido}")

    def juega_con(self, equipo_contrario):
        #Usar un random de goles
        #La seleccion que mete mas goles suma puntos
