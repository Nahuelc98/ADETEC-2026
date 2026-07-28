#import clase_seleccion
from clase_seleccion import SeleccionFutbol

class Jugador:
    """Definimos la clase jugador de la seleccion de fútbol"""
    def __init__(self, nombre, apellido, posicion):
        self.nombre=nombre
        self.apellido= apellido
        self.posicion = posicion
        # self.altura =altura
        # self.peso = peso
    def __str__(self):
        return f"{self.nombre} {self.apellido} juega de {self.posicion}"
    

class Delantero(Jugador):
    """Sub clase Delantero que hereda de la clase Jugador"""
    def __init__(self, nombre, apellido, posicion, prob_gol):
        super().__init__(nombre, apellido, posicion)
        self.goles=0
        self.probabilidad_goles=prob_gol

class Arquero(Jugador):
    """Sub clase Arquero que hereda de la clase Jugador"""
    def __init__(self, nombre, apellido, posicion,prob_atajada):
        super().__init__(nombre, apellido, posicion)
        self.prob_atajada=prob_atajada
        self.vallas_invictas=0
        


# messi =Delantero("Lionel", "Messi","Delantero",0.8)
# # Arqueros: Emiliano Martinez
# Geronimo Ruli

# #Defesores:
# Christian Romero
# Lisandro Martinez
# Nicolas Otamendi

# #Mediocampistas
# Leandro Paredes

# #Delanteros:
# Lionel Messi
# Julian Alvarez


