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

    print(f"{equipo1.upper()} vs {equipo2.upper()}")
    print("-" * 30)

    for ronda in range(1, 7):
        if ronda == 1:
            print("\n-- INICIO DEL PARTIDO --")
            time.sleep(3)
        elif ronda == 4:
            print("\nENTRETIEMPO...")
            time.sleep(4)
            print("\n-- INICIA EL SEGUNDO TIEMPO --")
            time.sleep(3)

        dado_e1 = random.randint(1, 6)
        dado_e2 = random.randint(1, 6)

        if dado_e1 > dado_e2:
            goles_e1 += 1
            print(f"GOOOL DE {equipo1.upper()}")
            time.sleep(3)
        elif dado_e2 > dado_e1:
            goles_e2 += 1
            print(f"GOOOL DE {equipo2.upper()}")
            time.sleep(3)
        else:
            print("JUGADA TRABADA, SIN GOL")
            time.sleep(3)

    print("-" * 30)
    print(f"RESULTADO FINAL: {equipo1.upper()} {goles_e1} - {goles_e2} {equipo2.upper()}")

    if goles_e1 > goles_e2:
        ganador = equipo1 # El ganador del partido es el equipo 1.
        perdedor = equipo2 # El equipo 2 perdio.
        return ganador, perdedor
    elif goles_e2 > goles_e1:
        ganador = equipo2 # El ganador del partido es el equipo 2.
        perdedor = equipo1 # El equipo 1 perdio.
        return ganador, perdedor
    else:
        print("\nEMPATE EN LOS 90 MINUTOS, VAMOS A LOS PENALES...") # Empatarón el partido, hay penales.
        time.sleep(4)

        ## LÓGICA DE SIMULACIÓN DE PENALES ##
        # 5 rondas...
        # Cada equipo tira un dado de direcciones, Una por cada dirección de pateo al arco:
        # Izquierda: arriba (IAR) y abajo (IAB). 
        # Al medio: arriba (MAR) y abajo (MAB).
        # Derecha: arriba (DAR) y abajo (DAB).
        # Si el equipo que patea saca una opción diferente al equipo que ataja, es gol para el equipo que patea.
        # Si el equipo que patea saca una opción igual al equipo que ataja, no suma gol para el equipo que patea.
        # Si en las 5 vueltas hay empate de goles de penal, se sigue pateando hasta que se saquen una diferencia.

        direcciones = ["IAR", "IAB", "MAR", "MAB", "DAR", "DAB"]
        penal_e1 = 0
        penal_e2 = 0

        sorteo_penales = [equipo1, equipo2]
        random.shuffle(sorteo_penales)
        patea_primero, patea_segundo = sorteo_penales
        print("\nSorteo de penales, patea primero...")
        time.sleep(2)
        print(f"\n{patea_primero} empieza pateando!!!\n")
        print("-- COMIENZAN LOS PENALES --")
        time.sleep(2)

        for ronda in range(1, 6):
            # Turno del equipo que patea primero: 
            print(f"\nVa a patear el jugador de {patea_primero} y...\n")
            time.sleep(2)           
            direccion_primero = random.choice(direcciones)
            direccion_segundo = random.choice(direcciones)

            if direccion_primero != direccion_segundo:
                penal_e1 += 1
                print(f"GOOL DE {patea_primero.upper()}")
            else:
                print(f"ATAJO EL ARQUERO DE {patea_segundo.upper()}")

            # Turno del equipo que patea segundo:
            print(f"\nVa a patear el jugador de {patea_segundo} y...\n")
            time.sleep(2)           
            direccion_primero = random.choice(direcciones)
            direccion_segundo = random.choice(direcciones)

            if direccion_segundo != direccion_primero:
                penal_e2 += 1
                print(f"GOOL DE {patea_segundo.upper()}")
            else:
                print(f"ATAJO EL ARQUERO DE {patea_primero.upper()}")

        if penal_e1 > penal_e2:
            ganador = equipo1 # El ganador del partido es el equipo 1.
            perdedor = equipo2 # El equipo 2 perdio.
            return ganador, perdedor
        elif penal_e2 > penal_e1:
            ganador = equipo2 # El ganador del partido es el equipo 2.
            perdedor = equipo1 # El equipo 1 perdio.
            return ganador, perdedor
        else:
            print("\nIgualan en la tanda regular, vamos por los penales mata mata...")
            while penal_e1 == penal_e2:
                # Turno del equipo que patea primero (mata mata):
                print(f"\nVa a patear el jugador de {patea_primero} y...\n")
                time.sleep(2)
                direccion_primero = random.choice(direcciones)
                direccion_segundo = random.choice(direcciones)               

                if direccion_primero != direccion_segundo:
                    penal_e1 += 1
                    print(f"GOOL DE {patea_primero.upper()}")
                else:
                    print(f"ATAJO EL ARQUERO DE {patea_segundo.upper()}")                      
        
                # Turno del equipo que patea segundo (mata mata):
                print(f"\nVa a patear el jugador de {patea_segundo} y...\n")
                time.sleep(2)
                direccion_primero = random.choice(direcciones)
                direccion_segundo = random.choice(direcciones)               

                if direccion_segundo != direccion_primero:
                    penal_e1 += 1
                    print(f"GOOL DE {patea_segundo.upper()}")
                else:
                    print(f"ATAJO EL ARQUERO DE {patea_primero.upper()}")            
  
            if penal_e1 > penal_e2:
                ganador = equipo1 # El ganador del partido es el equipo 1.
                perdedor = equipo2 # El equipo 2 perdio.
                return ganador, perdedor
            elif penal_e2 > penal_e1:
                ganador = equipo2 # El ganador del partido es el equipo 2.
                perdedor = equipo1 # El equipo 1 perdio.
                return ganador, perdedor





