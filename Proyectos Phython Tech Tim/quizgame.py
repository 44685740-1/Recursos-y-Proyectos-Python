from typing import SupportsComplex


print("Hola, bievenido a mi juego de preguntas") 
playing = input("¿queres jugar? ")
# != se puede usar para decir que una variable no es igual
#la funcion quit() se usa para ponerle fin al programa
# uso lower() para hacer todo minuscula
if playing.lower() != "yes":
    print("FIN")
    quit()

print("Bueno vamos a empezar el juego")
#uso el == porque estpy viendo si dos variables son iguales
score = 0
contador_preguntas = 0
#aqui utilizo la variable scrore como un contador de respuestas correctas
ansewr = input("¿en que año San Martin cruzo los andes? ").lower()
contador_preguntas = contador_preguntas + 1
if ansewr == "1816":
    print("Correct ")
    score = score +1
else:
    print("incorrect")

ansewr = input("¿en que año se firmo la cosntitucion de USA? ").lower()
contador_preguntas = contador_preguntas + 1
if ansewr == "1776":
    print("Correct ")
    score = score +1
else:
    print("incorrect")

ansewr = input("¿Quien es el creador de la bandera argentina? ").lower()
contador_preguntas = contador_preguntas + 1
if ansewr == "manuel belgrano":
    print("Correct ")
    score = score +1
else:
    print("incorrect")

ansewr = input("¿Quien fue el primer presidente de Estados Unidos? ").lower()
contador_preguntas = contador_preguntas + 1
if ansewr == "george washinton":
    print("Correct ")
    score = score +1
else:
    print("incorrect")

# uso el + para concatenar las variables siguiendo estando dentro de los parentesis
#saco el porcentaje
#uso str para convertir una variable en texto o un sting en ingles
#uso el contador de preguntas en vez de ponee el numero manualmente
print("tu puentaje funal de de: " + str(score) )
print("tue porcentaje de acirto fue del: " + str(score/contador_preguntas*100) + "%")
