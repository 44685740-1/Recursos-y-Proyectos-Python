#el diccionario sirve por ejeplo para uns lista de suoermercado
producto = {
    "nombre" : "libro",
    "precio" : "5.99",
    "cantidad" : "3"
}

print(type(producto))
print(dir(producto))
#tambien puedo solicitar la parte de los nombres de los satos o los propios items en cuestion
#usando keys o items respectivamente
print(producto.items())
print(producto.keys())
#se puede usar un diccionario dentro de una lista
productos2 = [
    {"Nomnre" : "libro", "precio" : "4.99"},
    {"Nomnre" : "laptop", "precio" : "10.99"}
]
