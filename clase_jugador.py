# importar clase_seleccion
from clase_seleccion import SeleccionFutbol

class Jugador:
    """Definimos la clase jugador de la seleccion de fútbol"""
    def __init__(self, nombre, apellido, posicion, numero):
        self.nombre=nombre
        self.apellido= apellido
        self.posicion = posicion
        self.numero = numero
        # self.altura =altura
        # self.peso = peso
    def __str__(self):
        return f"{self.nombre} {self.apellido} juega de {self.posicion} y usa la {self.numero}"
    

class Delantero(Jugador):
    """Sub clase Delantero que hereda de la clase Jugador"""
    def __init__(self, nombre, apellido, posicion, numero, prob_gol):
        super().__init__(nombre, apellido, posicion, numero)
        self.goles=0
        self.probabilidad_goles=prob_gol

class Arquero(Jugador):
    """Sub clase Arquero que hereda de la clase Jugador"""
    def __init__(self, nombre, apellido, posicion, numero, prob_atajada):
        super().__init__(nombre, apellido, posicion, numero)
        self.prob_atajada=prob_atajada
        self.vallas_invictas=0
