from clase_seleccion import SeleccionFutbol
from clase_jugador import Jugador

lionel_messi = Jugador("Lionel","Messi","Delantero")
rodri_depaul = Jugador("Rodrigo", "De Paul", "Mediocampista")

sel_argentina = SeleccionFutbol("Argentina", "Lionel Scaloni", 3,"H")

sel_argentina.convocar(lionel_messi)
sel_argentina.convocar(rodri_depaul)

n=0
while n < 4:
    print("Convoque un jugador: ")
    nombre=input("Nombre del jugador: ")
    apellido=input("Apellido del jugador: ")
    pos = input("Posicion: ")

    jugador_nuevo=Jugador(nombre,apellido,pos)
    sel_argentina.convocar(jugador_nuevo)
    n +=1

sel_argentina.mostrar_plantel()

sel_mexico=SeleccionFutbol("Mexico","Juan Perez",0,"H")
sel_mexico=SeleccionFutbol("España","De la fuente",0,"A")
