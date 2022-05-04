MiString = "Ahuitz caracciolo"
#se puede itilizar la funcion dir para que nos indique cules son las funciones y propiedades de cada comando
print(dir(MiString))
#se puede concatenar como abajo, de cualquiera de las dos formas
print("my name is " + MiString)
print(f"My name is {MiString}")
print(MiString.upper())
print(MiString.lower())
print(MiString.swapcase())
print(MiString.capitalize())
print(MiString.replace("Ahuitz", "caracciolo"))
print(MiString.count(" "))
print(MiString.startswith("Ah"))
print(MiString.split("i"))
print(MiString.find("i"))
print(len(MiString))

print(MiString.isnumeric())
# tambien puedo mostrar en pantalla un caracter del texto que introduje, indicando el numero de la casilla donde 
# se encuentra el caraccter necesitado
print(MiString[3])
#apretar control + shift + p para opciones phython y buscar opcion para comentar
#tambien se puede utilizar comillas triple para varias lineas de comentarios
"""""
est es un comtario
"""