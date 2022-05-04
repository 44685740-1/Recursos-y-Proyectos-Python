#importo una documentacion con valores aleatorios
import random

def  adivina_el_número ( x ):


    print ( "============================" )
    print ( "¡Bienvenido (a) al Juego!" )
    print ( "============================" )
    print ( "Tu meta es adivinar el número generado por la computadora." )
    #randint devuelve un numero entero cualquiera
    número_aleatorio  = random.randint( 1 , x ) # número aleatorio entre 1 y x.

    # La predicción es 0 primero para que no coincida con el número aleatorio. 
    predicción  =  0

    # Continuar prediciendo el número hasta que la predicción sea correcta.
    #se usa != para decir que es diferente
    #int se usa para convertir ewn entero
    while  predicción   !=  número_aleatorio :
        # El usuario ingresa un número.
        predicción  =  int ( input ( f'Adivina un número entre 1 y { x } : ' ))
        # Si el número es menor que el número aleatorio, se 
        # muestra un mensaje.
        if  predicción  <  número_aleatorio :
            print ( 'Intenta otra vez. Este número es muy pequeño.' )
        # Si el número es mayor que el número aleatorio, se
        # muestra un mensaje.
        elif  predicción  >  número_aleatorio :
            print ( 'Intenta otra vez. Este número es muy grande.' )

    # El ciclo o bucle se detiene cuando el usuario adivina el número
    # correctamente y se muestra un mensaje final.
    print ( f'¡Felicitaciones! Adivinaste el número { número_aleatorio } correctamente. ' )

# Llamar a la función
adivina_el_número ( 10 )
