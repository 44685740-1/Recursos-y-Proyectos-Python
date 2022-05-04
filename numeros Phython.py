# los tipos de numeros mas comunes entero (int) y decimal (float)
print(type(9))
print(type(10.1))
print(1+1)
#si multiplico un decimal por un entero me lo devuelve como edecimal
#por ejemplo 1 + 1.0 = 2.0
#para elevar un numero a otro se hace como en la linea de abajo
print(3**3)
#para sacar el residuo de una division
print(10 % 3)

#aunque se escriba un numero en el print se toma como un string y no como un numero por lo cual hay
# que indicar que se trata de un numero entero o decimal

edad = input("ingrese su edad: ")
Nueva_Edad = int(edad) + 5
print(Nueva_Edad)
