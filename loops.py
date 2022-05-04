from typing import Counter


comidas= ["banana", "manzanas", "naranjas", "piñas", "peras"]
#se puede usar break para terminar con el loop 
#se puede usar comtiniu para seguir con el loop

for comidas in comidas:
    if comidas=="manzanas":
        print("tienes que compra esto")
    print(comidas)

#se puede usar con un rango
for letra in "hola":
    print(letra)

#ahora veremos otro bucle llamado while
#tambien usaremos contadores
Count=4
while Count<=10:
    print(Count)
    Count=Count + 1
