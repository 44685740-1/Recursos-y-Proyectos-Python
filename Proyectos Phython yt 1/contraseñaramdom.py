import random
lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "[]{}#*;:-_"
all = lower + upper + numeros + simbolos 
length = 9
password = "".join(random.sample(all,length))
print("su nueva contraseña es: , password")
