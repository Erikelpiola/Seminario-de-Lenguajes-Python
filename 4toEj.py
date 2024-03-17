numeros = input ("Ingrese una lista de numeros enteros separados por espacios: ")
numeros = [int (numero) for numero in numeros.split()]
print("Entre los numeros dados, se imprimiran los pares: ")
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(numero)
#Introduccion al concepto de lista aprendido