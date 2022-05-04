#las funciones que ya utilizamos son print dir type
#usamos def y parentesis para que sepa de que se trata de una funcion
#funcion sin argumentos y llamandola para que funcione
def hola():
    print("hola mundo")

hola()

#funcion con argumentos
#si el usuario no pone ningun argumento por defecto dira person porque eso indicamos en name
def hellow(name=" persona"):
    print("hellow" + name)

hellow(" ahuitz")
hellow(" juan")
hellow(" carlos")
hellow()

#ahora con numeros uso return

def add(numero_1, numero_2):
    return numero_1 + numero_2

print(add(10, 5))

#a continuacion usaremos las funciones lambda, aqui no hace falta usar return

add2 = lambda num1, num2: num1 + num2

print(add2(4,3))
