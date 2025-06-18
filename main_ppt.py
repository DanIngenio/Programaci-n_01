# -*- coding: utf-8 -*-

# Importar libreria necesaria 
import random

# --------------------------------------------------------------- Paso 1: Mostrar mensaje de bienvenida 
print("¡Bienvenido al juego Piedra - Papel - Tijera! ")
print("""
██████╗ ██████╗ ████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╔╝██████╔╝   ██║   
██╔═══╝ ██╔═══╝    ██║   
██║     ██║        ██║   
╚═╝     ╚═╝        ╚═╝   
""")

print(" Desarrolado por: Daniel Ilbay \n\n\n")


while True:
    print("-------------------------El juego Inicio :D \n")
    
    n=int(input("Ingrese el número de partidas: \n")) # -------- Paso 2: Ingresar el número de partidas 

    p_jugador   =0                                    # -------- Paso 3: Inicializar el marcado
    p_computador=0

    op_jugada=['Piedra','Papel','Tijera']

    print("-> Ejegir una de las siguiente Opciónes: \n")
    print(" Presione 1: Piedra")
    print(" Presione 2: Papel")
    print(" Presione 3: Tijera")

    for i in range(n):
        print("-------------------------  Partida número",i+1)

        ii            = int(input("Ingrese su jugada: \n"))-1 # Paso 4: Solicitar la opción del Jugador 
        op_jugador    = op_jugada[ii]

        jj            = random.randint(0, 2)
        op_computador = op_jugada[jj]                        # Paso 5: Solicitar la opción del computador 


        print(f"\t {op_jugador} vs {op_computador} \n")

        if op_jugador==op_computador:                       # Paso 6: Comparar las jugadas 
            # misma jugada no se cuenta 
            pass
        elif op_jugador=='Piedra' and op_computador=='Papel':
            p_computador=p_computador+1

        elif op_jugador=='Piedra' and op_computador=='Tijera':
            p_jugador=p_jugador+1

        elif op_jugador=='Papel' and op_computador=='Piedra':
            p_jugador=p_jugador+1

        elif op_jugador=='Papel' and op_computador=='Tijera':
            p_computador=p_computador+1

        elif op_jugador=='Tijera' and op_computador=='Piedra':
            p_computador=p_computador+1

        elif op_jugador=='Tijera' and op_computador=='Papel':
            p_jugador=p_jugador+1

    print("-------------------------Fin de la partidas \n") 
    
    print(f"Partidas ganadas Jugador    :{p_jugador}")      # Paso 7: Comparar Marcador 
    print(f"Partidas ganadas Computador :{p_computador}")
    
    print("------------------------- RESUMEN \n")          # Paso 8 : Comparar Marcador 
    if p_jugador > p_computador:
        print("Felidades eres el Ganador")
    elif p_jugador < p_computador:
        print("Perdiste, mejor suerte para la próxima")
    else:
        print("Muy bien es un Empate")
        
    print("\n\nIngrese 1 para jugar Nuevamente 0 para Salir") # Paso 8: Jugar nuevamente 
    salir=int(input(":"))
    
    if salir!=1:
        break
        
    print("\n\n ----- GRACIAS, NOS VEMOS PRONTO ----")
    