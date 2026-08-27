import random
import time

## LÓGICA DE SIMULACIÓN ##
# Son 6 rondas, 3 el primer tiempo, 3 el segundo tiempo.
# En cada ronda los dos equipos tiran un dado:
# El que saque el número mayor mete un gol.
# Si ambos equipos sacan el mismo número, no mete un gol ninguno de los dos.
# Al final de las 6 rondas, el equipo con mas goles gana y si tienen la misma cantidad de goles es un empate.

# Función para simular partido:
def simular_partido(equipo1, equipo2):
    goles_e1 = 0
    goles_e2 = 0

    print(f"{equipo1} vs {equipo2}")
    print("-" * 30)

    for ronda in range(1, 7):
        if ronda == 1:
            print("\n-- INICIO DEL PARTIDO --")
        elif ronda == 4:
            print("\n-- ENTRETIEMPO --")
            time.sleep(2)
            print("\n-- INICIA EL SEGUNDO TIEMPO --")

        dado_e1 = random.randint(1, 6)
        dado_e2 = random.randint(1, 6)

        if dado_e1 > dado_e2:
            goles_e1 += 1
            print(f"GOOOL DE {equipo1.upper()}")
        elif dado_e2 > dado_e1:
            goles_e2 += 1
            print(f"GOOOL DE {equipo2.upper()}")
        else:
            print("JUGADA TRABADA, SIN GOL")

    print("-" * 30)
    print(f"RESULTADO FINAL: {equipo1.upper()} {goles_e1} - {goles_e2} {equipo2.upper()}")

    while goles_e1 == goles_e2:
        print("EMPATE EN LOS 90 MINUTOS, VAMOS A LOS PENALES...")
        time.sleep(2)

    ## LÓGICA DE SIMULACIÓN DE PENALES ##
    # 5 rondas...
    # Cada equipo tira un dado de 9 caras, Una por cada dirección de pateo al arco:
    # Izquierda: arriba (IAR), al medio (IM), abajo (IAB). 
    # Al medio: arriba (MAR), al medio (MM), abajo (MAB).
    # Derecha: arriba (DAR), al medio (DM), abajo (DAB).
    # Si el equipo que patea saca una opción diferente al equipo que ataja, es gol para el equipo que patea.
    # Si el equipo que patea saca una opción igual al equipo que ataja, no suma gol para el equipo que patea.
    # Si en las 5 vueltas hay empate de goles de penal, se sigue pateando hasta que se saquen una diferencia.

        direcciones = ["IAR", "IM", "IAB", "MAR", "MM", "MAB", "DAR", "DM", "DAB"]
        penal_e1 = 0
        penal_e2 = 0

        sorteo_penales = [equipo1, equipo2]
        random.shuffle(sorteo_penales)
        patea_primero, patea_segundo = sorteo_penales
        print("Sorteo de penales, patea primero...")
        time.sleep(1)
        print(f"{patea_primero} empieza pateando")
        print("-- COMIENZAN LOS PENALES --")

        for ronda in range(1, 6):
            # Turno del equipo que patea primero: 
            print(f"Va a patear el jugador de {patea_primero} y...")
            time.sleep(2)           
            patea_primero = random.choice(direcciones)
            patea_segundo = random.choice(direcciones)

            if patea_primero != patea_segundo:
                penal_e1 += 1
                print(f"GOOL DE {patea_primero.upper()}")
            else:
                print(f"ATAJO EL ARQUERO DE {patea_segundo.upper()}")

            # Turno del equipo que patea segundo:
            print(f"Va a patear el jugador de {patea_segundo} y...")
            time.sleep(2)
            patea_primero = random.choice(direcciones)
            patea_segundo = random.choice(direcciones)

            if patea_segundo != patea_primero:
                penal_e2 += 1
                print(f"GOOL DE {patea_segundo.upper()}")
            else:
                print(f"ATAJO EL ARQUERO DE {patea_primero.upper()}")

        if penal_e1 == penal_e2:
            print("Igualan en la tanda regular, vamos por los penales mata mata...")
            while penal_e1 == penal_e2:
                # Turno del equipo que patea primero (mata mata):
                print(f"Va a patear el jugador de {patea_primero} y...")
                time.sleep(2)
                patea_primero = random.choice(direcciones)
                patea_segundo = random.choice(direcciones)               

                if patea_primero != patea_segundo:
                    penal_e1 += 1
                    print(f"GOOL DE {patea_primero.upper()}")
                else:
                    print(f"ATAJO EL ARQUERO DE {patea_segundo.upper()}")                      
        
                # Turno del equipo que patea segundo (mata mata):
                print(f"Va a patear el jugador de {patea_segundo} y...")
                time.sleep(2)
                patea_primero = random.choice(direcciones)
                patea_segundo = random.choice(direcciones)               

                if patea_primero != patea_segundo:
                    penal_e1 += 1
                    print(f"GOOL DE {patea_segundo.upper()}")
                else:
                    print(f"ATAJO EL ARQUERO DE {patea_primero.upper()}")            

        else:
            if penal_e1 > penal_e2:
                print(f"GANOOO {equipo1.upper()}")
            else:
                print(f"GANOOO {equipo2.upper()}")    






