demo_lista = [1, "Ahuitz" , 1.34 , True, [1,2,3]]
colors = ["rojo", "azul", "amarillo"]
#a continuacion pongo una tupla para hacer una lista

Lista_Numeros = list((1,2,3))
#la clase de tipo de datos en esta lista numerica nos indica que es list y no entero o decimal
print(type(Lista_Numeros))

#el siguiente nos muestra los numeros que se encuentran en nuestro definido rango

Rango = list(range(1,10))
print(Rango)

#el siguiente nos cuenta la cantidad de datos que se encuentran en la lista de la cual pedimos informacion
print(len(demo_lista))

#el siguiente nos muestra un de los datos que le indicamos de una lista definida, indicamos el espacio
print(colors[1])

#tambien se puede cambiar un dato de nuestra lista por ejemplo de colors

print(colors)
colors[2] = "violeta"
print(colors)

#utilizar dir para saber las funciones
print(dir(colors))

#utilizar append para añadir solo un dato mas
colors.append("verde")

#utilizo extend para agregar dos o mas elementos a nuestra lista hay que utilizar una tupla para que salga bien
colors.extend(["naranja", "morado"])
colors.extend("naranja", "morado")

#usando inset puedo insetar en el lugar que deseo

colors.insert(1, "negro")

#en el siguiente coloco un dato en el ultimo espacion usando len para que cuente los espacios de la lista
colors.insert(len(colors), "blanco")

#para sacar el ultimo dato puedo usar pop
colors.pop()

#puedo utlizar remove para remover un dato de la lista en especifico
colors.remove("rojo")

#tambien puedo usar pop para remover datos segun el indice de la lista
colors.pop(1)

#puedo usar clear para remover todos los elementos de la lista
colors.clear()

#puedo usar sort para ordenar alguna lista
colors.sort()

#utilizo reverse y true para ordenar al reves segun el abecedario
colors.sort(reverse=True)

#tambien puede ver el indice de alguno de los datos de mi lista
print(colors.index("azul"))

#tambien puedo contar cuantas veces se repie un elemento usando count
print(colors.count("azul"))
