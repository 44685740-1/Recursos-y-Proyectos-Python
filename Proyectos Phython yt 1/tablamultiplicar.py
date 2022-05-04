print("ingrese el numero que desea saber su tabla de multiplicar")
num = int(input())
print("TABLA")
#estamos usando la coma , para concatenar "" para texto y lo otro solo entre parenteis
for i in range(0,11):
    resultado = i*num
    print(num, "x", i, " = ", resultado)


