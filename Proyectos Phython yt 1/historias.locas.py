organizacion = "con You Tube"
#las tres son equivalentes
# print("se puede aprender a programar usando " + organizacion)
# print("se puede aprender a programar usando {}".format(organizacion))
# print( f"se puede aprender a programar usando {organizacion}")

#se puede usar imput para solicitar al usuario que ingrese informaciom
adj = input("adjetivo: ")
verbo1= input("verbo: ")
verbo2= input("verbo 2: ")
sustantivoP = input("sustantivo (plural): ")

#usando alt + z una linea larga se divide en varias para que quede bonito

listaloca = f"¡programar es tan {adj}! siempre me emocina porque me encanta {verbo1} problemas. ¡aprende a {verbo2} con You Tube y alcanza tus {sustantivoP}"

print(listaloca)