import string

import random


from palabrasahorcado import palabras


def obtener_palabra_valida(palabras):
#seleccioo una palabra al azar de la lista de palabra
    palabra = random.choice(palabras)
    while "-" in palabra or " " in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()



def ahorcado():
    print("bienvenido al juego del ahorcado ")

    palabras = obtener_palabra_valida(palabras)
    # usamos ascii_uppercase para que nos devuleva el abecedario en mayusculas
    # un set contiene una cadena de datoa que no se repiten entre si
    letras_por_adivinar = set(palabras)
    letras_adivinadas = set()
    vidas = 7
    abedecedario = set(string.ascii_uppercase)

while len(letras_por_adivinar) > 0 and vidas > 0:
    print
