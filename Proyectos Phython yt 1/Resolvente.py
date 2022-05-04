import math
print("Bienvenido al programa donde podras calcular la formula resovente solo indicando los valores")
#utilizo float para convertir el valor en un valor numerico
#podria haber utilizado el \n para que quede mas bonito
#el discriminante es lo que determina si hay una, dos o todos los reales de solucion
a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

if a ==0:
    print("el coeficiente a no puede ser igual a 0 ERROR")
else:
    discriminante = b**2 - 4 * a * c
    if discriminante >= 0:
        if discriminante == 0:
            x = -b / (2*a)
            print("la raiz unica es {:,3f}".format(x))
        else: 
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            print("La raíz real x1 es {:.3f}".format(x1))
            print("La raíz real x2 es {:.3f}".format(x2))
    else:
        #utilizo abs que quiere decir absoluto
        discriminante = abs(discriminante)
        parteReal = -b / (2 * a)
        ParteImaginaria = math.sqrt(discriminante) / (2 * a)
        print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, ParteImaginaria))
        print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, ParteImaginaria))
