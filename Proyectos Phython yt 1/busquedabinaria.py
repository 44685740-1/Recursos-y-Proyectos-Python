import random
import time


def busqueda_ingenua(lista,objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

Mi_lista = [1,2,3,4,5,6,7,8,9,10]
print(busqueda_ingenua(Mi_lista,3))


def busqueda_binaria(lista,objetivo, Limite_Inferiro= None, Limite_superior= None):
    if Limite_Inferiro is None:
        Limite_Inferiro= 0
    if Limite_superior is None:
        Limite_superior= len(lista) - 1

    if Limite_superior < Limite_Inferiro:
        return -1
    #la operacion // divide y trunca el resultado
    punto_medio = (Limite_Inferiro + Limite_superior) // 2


    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista,objetivo,Limite_Inferiro,punto_medio-1)
    else:
        return busqueda_binaria(lista,objetivo, Limite_superior, punto_medio + 1)


if  __name__ == '__main__' :
    # Crear una lista ordenada con 10000 números aleatorios.
    tamaño  =  10000
    conjunto_inicial  =  set ()
#usamos add para gregar
    while  len ( conjunto_inicial ) <  tamaño :
        conjunto_inicial . add ( random . randint ( - 3 * tamaño , 3 * tamaño ))
#usamos sorted para que nos ordene de forma de escala de abajo hacia arriba y list para convertir en lista
    lista_ordenada  =  sorted ( list ( conjunto_inicial ))

    # Medir el tiempo de búsqueda ingenua.
    inicio  =  time . time ()
    for  objetivo  in  lista_ordenada :
        busqueda_ingenua ( lista_ordenada , objetivo )
    fin  =  time . time ()
    print ( f"Tiempo de búsqueda ingenua: { fin  -  inicio } segundos." )

    # Medir el tiempo de búsqueda binaria.
    inicio  =  time . time ()
    for  objetivo  in  lista_ordenada :
        busqueda_binaria ( lista_ordenada , objetivo )
    fin  =  time . time ()
    print ( f"Tiempo de búsqueda binaria: { fin  -  inicio } segundos." )

