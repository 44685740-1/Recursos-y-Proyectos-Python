import random

#uso choice para elejir
#se puede usar el simbolo \n para finalizar una linea y que quede mas prolijo cuando se ejecuta
def jugar():
    usuario = input("escoge una opcion: (pi) para piedra, (pa) para papel,(ti) para tijera.\n").lower()
    computadora = random.choice(["pi", "pa", "ti"])
    if usuario == computadora:
        return "empate"
    if gano_el_jugador(usuario,computadora):
        return "ganaste"
    return "perdiste"
    

def gano_el_jugador(jugador, oponente):
    #voy a hacer un verdadero y falso en cada posibilidad del juego
    if ((jugador == "pi" and oponente == "ti")
        or (jugador == "ti" and oponente == "pa")
        or (jugador == "pa" and oponente == "pi")):
        return True
    else:
        return False



print(jugar())



