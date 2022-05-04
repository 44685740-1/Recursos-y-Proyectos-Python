#en la consola de phython hay que escribir 3==3 para saber comparar y saber si son o no iguales los valores
x = 9
#usar la tecla tabulador para dejar un espacio y que funcione
if x < 30:
    print("x es menor que 30")

if x == 30:
    print("x es 30")
else:
    print("x no es 30")

#tabien exite elif que nos permite colocar otra posibilidad antes del else
if x == 30:
    print("x es 30")
elif x==20:
    print("x es 20")
else:
    print("x no es 30")

#se puede imponer dos condiciones es decir dos if
nombre="ahuitz"
apellido="caraciolo"
#para el if si utilizo ==
if nombre=="ahuitz":
    if apellido=="caracciolo":
        print("vos sos ahuitz caracciolo")
    else:
         print("vos no sos ahuitz caracciolo")

#se puede utilizar conectores logicos como and not o or en los if
if x>2 and x<10:
    print("x es mayor que dos y menor a 10")
if x>2 or x<20:
    print("x es mayor que dos y menor a 20")
if (not(x=="y")):
    print("x no es igual a y ")
    