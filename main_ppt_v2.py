# -*- coding: utf-8 -*-

# Importar libreria necesaria 
import random
# ------------------- Funciones---------------
def f_mostrar_menu_principal(lista_op):
    """
    Muestra el menú principal y captura la selección del jugador.
    Valida si la opción está en la lista de opciones válidas.
    Retorna la opción seleccionada como entero.
    """
    while True:
        print("Bienvenidos")    
        print("-> Menu principal: \n")
        print(" Presione 1: Jugar")
        print(" Presione 2: Reglas del juego")
        print(" Presione 3: Salir del juego")
        op = input("Ingrese Opción: \n")
        opv = f_validar_entrada_numerica(op, lista_op)
        if opv != "op_incorrecto":
            return opv
        else:
            print("⚠ Opción inválida. Intente nuevamente.\n")
def f_validar_entrada_numerica(op, lista_op):
    """
    Valida que la entrada 'op' sea numérica y que esté dentro de las opciones en lista_op.
    Retorna 'op_incorrecto' si no es numérico o no está en la lista.
    En caso contrario, retorna 'op' como entero.
    """
    if str(op).isdigit():
        if int(op) in lista_op:
            return int(op)
    return "op_incorrecto"    

def f_menu_jugar(lista_op):
    """
    Muestra el menú de juego y valida la entrada del usuario con opciones [1, 2, 3, 4].

    1: Inicia el juego contra la computadora.
    2: Inicia el juego contra otro jugador.
    3: Ver estadística de la última partida (mensaje si no hay partidas).
    4: Regresa al menú principal.

    Retorna la opción elegida como entero.
    """
    while True:
        print("\n-> Menú de opciones para Jugar:")        
        print(" Presione 1: Contra la computadora")
        print(" Presione 2: Multijugador (2 jugadores)")
        print(" Presione 3: Ver estadísticas de la última partida")
        print(" Presione 4: Regresar al menú principal")
        op = input("Ingrese una opción: ")
        opv = f_validar_entrada_numerica(op, lista_op)
        if opv != "op_incorrecto":
            return opv
        else:
            print("⚠ Opción inválida. Intente nuevamente.\n")   

def f_juego_modo_contra_computadora(nombre, cantidad=None):
    """
    Ejecuta el juego en modo contra la computadora.
    Si se define un número de partidas, se juega esa cantidad; 
    caso contrario, se juega hasta que el usuario decida salir.
    """
    print(f"------------------------- El juego inició contra computador :D \n")
    
    g_jugador = p_jugador = e_jugador = 0
    g_pc = p_pc = e_pc = 0
    op_jugada = ['Piedra', 'Papel', 'Tijera']
    detalles = []

    partida = 1
    while True:
        print(f"\n------------------------- Partida número {partida}")
        print("-> Elegir una de las siguientes opciones: ")
        print(" 1: Piedra")
        print(" 2: Papel")
        print(" 3: Tijera")
        
        # Entrada válida del jugador
        while True:
            jugada = input(f"{nombre}, ingrese su jugada (1-3): ")
            jugada_val = f_validar_entrada_numerica(jugada, [1, 2, 3])
            if jugada_val != "op_incorrecto":
                break
            print("⚠ Entrada inválida. Intente nuevamente.")

        op_jugador = op_jugada[jugada_val - 1]
        jj = random.randint(0, 2)
        op_computador = op_jugada[jj]

        print(f"\t{nombre}: {op_jugador} vs Computadora: {op_computador}")

        # Determinar resultado
        if op_jugador == op_computador:
            print("Resultado: Empate esta ronda.")
            detalles.append(f"Partida {partida}: {nombre} empató - Computadora empató")
            e_jugador += 1
            e_pc += 1
        elif (op_jugador == 'Piedra' and op_computador == 'Tijera') or \
             (op_jugador == 'Papel' and op_computador == 'Piedra') or \
             (op_jugador == 'Tijera' and op_computador == 'Papel'):
            print("Resultado: ¡Ganaste esta ronda!")
            detalles.append(f"Partida {partida}: {nombre} ganó - Computadora perdió")
            g_jugador += 1
            p_pc += 1
        else:
            print("Resultado: La computadora gana esta ronda.")
            detalles.append(f"Partida {partida}: {nombre} perdió - Computadora ganó")
            g_pc += 1
            p_jugador += 1

        partida += 1

        # Si se definió número de partidas, verificar si ya terminó
        if cantidad is not None:
            if partida > cantidad:
                break
        else:
            seguir = input("¿Desea jugar otra partida? (si/no): ").lower()
            if seguir != "si":
                break

    total_partidas = partida - 1
    print(f"\n-------------------------------- Número de partidas realizadas: {total_partidas}")
    for linea in detalles:
        print(linea)

    print("\n-------------------------------- Estadísticas:")
    print(f"{nombre}     : ganó {g_jugador}, perdió {p_jugador}, empató {e_jugador}")
    print(f"Computadora : ganó {g_pc}, perdió {p_pc}, empató {e_pc}")

    # Retornar resumen
    return {
        "modo": "computadora",
        "total": total_partidas,
        "detalle": detalles,
        "estadisticas": {
            nombre: {"gano": g_jugador, "perdio": p_jugador, "empato": e_jugador},
            "Computadora": {"gano": g_pc, "perdio": p_pc, "empato": e_pc}
        }
    }

def f_juego_modo_multijugador(nombre1, nombre2, cantidad=None):
    """
    Ejecuta el juego en modo multijugador.
    Si se define un número de partidas, se juega esa cantidad; 
    si no, se repite hasta que los jugadores decidan terminar.
    """
    print(f"------------------------- El juego inició en modo Multijugador 🧑‍🤝‍🧑 \n") 

    op_jugada = ['Piedra', 'Papel', 'Tijera']

    g1 = p1 = e1 = 0
    g2 = p2 = e2 = 0
    detalles = []
    partida = 1

    while True:
        print(f"\n------------------------- Partida número {partida}")
        print("-> Elegir una de las siguientes opciones:")
        print(" 1: Piedra")
        print(" 2: Papel")
        print(" 3: Tijera")

        # Jugador 1
        while True:
            j1 = input(f"{nombre1}, ingrese su jugada (1-3): ")
            j1_val = f_validar_entrada_numerica(j1, [1, 2, 3])
            if j1_val != "op_incorrecto":
                jugada1 = op_jugada[j1_val - 1]
                break
            else:
                print("⚠ Entrada inválida. Debe ser 1, 2 o 3.\n")

        # Jugador 2
        while True:
            j2 = input(f"{nombre2}, ingrese su jugada (1-3): ")
            j2_val = f_validar_entrada_numerica(j2, [1, 2, 3])
            if j2_val != "op_incorrecto":
                jugada2 = op_jugada[j2_val - 1]
                break
            else:
                print("⚠ Entrada inválida. Debe ser 1, 2 o 3.\n")

        print(f"\t{nombre1}: {jugada1} vs {nombre2}: {jugada2}")

        if jugada1 == jugada2:
            print("Resultado: Empate esta ronda.")
            detalles.append(f"Partida {partida}: {nombre1} empató - {nombre2} empató")
            e1 += 1
            e2 += 1
        elif (jugada1 == 'Piedra' and jugada2 == 'Tijera') or \
             (jugada1 == 'Papel' and jugada2 == 'Piedra') or \
             (jugada1 == 'Tijera' and jugada2 == 'Papel'):
            print(f"Resultado: ¡{nombre1} gana esta ronda!")
            detalles.append(f"Partida {partida}: {nombre1} ganó - {nombre2} perdió")
            g1 += 1
            p2 += 1
        else:
            print(f"Resultado: ¡{nombre2} gana esta ronda!")
            detalles.append(f"Partida {partida}: {nombre1} perdió - {nombre2} ganó")
            g2 += 1
            p1 += 1

        partida += 1

        if cantidad is not None and partida > cantidad:
            break
        elif cantidad is None:
            seguir = input("¿Desean jugar otra partida? (si/no): ").lower()
            if seguir != "si":
                break

    total = partida - 1
    print(f"\n-------------------------------- Número de partidas realizadas: {total}")
    for linea in detalles:
        print(linea)

    print("\n-------------------------------- Estadísticas:")
    print(f"{nombre1}: ganó {g1} partidas, perdió {p1} partidas, empató {e1} partida{'s' if e1 != 1 else ''}")
    print(f"{nombre2}: ganó {g2} partidas, perdió {p2} partidas, empató {e2} partida{'s' if e2 != 1 else ''}")

    return {
        "modo": "multijugador",
        "total": total,
        "detalle": detalles,
        "estadisticas": {
            nombre1: {"gano": g1, "perdio": p1, "empato": e1},
            nombre2: {"gano": g2, "perdio": p2, "empato": e2}
        }
    }


def f_mostrar_estadisticas(ultima_partida):
    """
    Muestra el resumen y las estadísticas de la última partida si existen.
    Si no hay datos, informa al usuario que no hay estadísticas disponibles.
    """
    if ultima_partida is None:
        print("📊 No hay estadísticas registradas recientemente.")
        return

    print("\n📊 Resumen:")
    print(f"Número de partidas realizadas: {ultima_partida['total']}")
    for linea in ultima_partida["detalle"]:
        print(linea)

    print("\n📊 Estadísticas:")
    for jugador, datos in ultima_partida["estadisticas"].items():
        print(f"{jugador}: ganó {datos['gano']}, perdió {datos['perdio']}, empató {datos['empato']}")

def f_mostrar_reglas():
    """
    Muestra las reglas del juego en todas sus modalidades y recomendaciones básicas.
    """
    print("\n📜 REGLAS DEL JUEGO: PIEDRA, PAPEL O TIJERA\n")
    print("Este es un juego clásico de estrategia simple pero divertida.")
    print("El objetivo es vencer la elección de tu oponente utilizando la lógica del siguiente sistema:\n")
    
    print(" 🪨 Piedra aplasta a ✂️ Tijera")
    print(" ✂️ Tijera corta a 📄 Papel")
    print(" 📄 Papel envuelve a 🪨 Piedra\n")

    print("🔁 Modalidades:")
    print(" 1. Contra la Computadora: El sistema generará su jugada al azar.")
    print(" 2. Multijugador: Dos jugadores competirán ingresando sus jugadas.")
    print(" 3. Empates: Si ambos eligen la misma opción, la ronda termina empatada.\n")
    
    print("🏆 Gana quien acumule más victorias en el número de partidas que tú determines.\n")

    print("⚠ Recomendaciones:")
    print(" - Asegúrate de ingresar números válidos (1, 2 o 3) al elegir tu jugada.")
    print(" - Juega limpio y no mires la jugada de tu oponente si están en multijugador.\n")

    print("🎮 ¡Buena suerte y que gane el mejor!\n")       

def f_preguntar_modo_partidas():
    """
    Pregunta si se desea definir un número de partidas y retorna la cantidad o None.
    """
    while True:
        respuesta = input("¿Desea definir un número de partidas? (si/no): ").lower()
        if respuesta == "si":
            while True:
                cantidad = input("Ingrese el número de partidas que desea jugar: ")
                if cantidad.isdigit() and int(cantidad) > 0:
                    return int(cantidad)
                else:
                    print("⚠ Ingrese un número entero positivo.")
        elif respuesta == "no":
            return None
        else:
            print("⚠ Respuesta inválida. Escriba 'si' o 'no'.")   
def f_pedir_nombres(modo):
    """
    Solicita y retorna el o los nombres de los jugadores según el modo de juego.
    """
    if modo == "computadora":
        nombre1 = input("Ingrese su nombre: ")
        return nombre1, None
    elif modo == "multijugador":
        nombre1 = input("Ingrese el nombre del Jugador 1: ")
        nombre2 = input("Ingrese el nombre del Jugador 2: ")
        return nombre1, nombre2
    else:
        return None, None
# ------------------- MAIN -------------------
def main():
    """
    Controla el flujo principal del juego Piedra, Papel o Tijera.
    Permite al usuario seleccionar entre jugar, ver reglas o salir.
    Gestiona los modos de juego y muestra estadísticas al finalizar.
    """
    ultima_partida = None

    while True:
        opcion = f_mostrar_menu_principal([1, 2, 3])
        
        if opcion == 1:
            while True:
                eleccion_jugar = f_menu_jugar([1, 2, 3, 4])
                
                if eleccion_jugar == 1:
                    print("Inicia juego contra la computadora...\n")
                    nombre, _ = f_pedir_nombres("computadora")
                    cantidad = f_preguntar_modo_partidas()
                    ultima_partida = f_juego_modo_contra_computadora(nombre, cantidad)
                    f_mostrar_estadisticas(ultima_partida)

                elif eleccion_jugar == 2:
                    print("Inicia juego multijugador...\n")
                    nombre1, nombre2 = f_pedir_nombres("multijugador")
                    cantidad = f_preguntar_modo_partidas()
                    ultima_partida = f_juego_modo_multijugador(nombre1, nombre2, cantidad)
                    f_mostrar_estadisticas(ultima_partida)

                elif eleccion_jugar == 3:
                    f_mostrar_estadisticas(ultima_partida)
                    input("\nPresione Enter para regresar al menú de juego...")

                elif eleccion_jugar == 4:
                    break  # Regresa al menú principal

        elif opcion == 2:
            f_mostrar_reglas()

        elif opcion == 3:
            print("👋 Saliendo del juego. ¡Hasta pronto!")
            break

# ------------------- EJECUCIÓN -------------------
if __name__ == "__main__":
    main()