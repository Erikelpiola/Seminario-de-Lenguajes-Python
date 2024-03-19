numeros = input ("Ingrese una lista de numeros enteros separados por espacios: ")
numeros = [int (numero) for numero in numeros.split()]
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print("Los numeros pares de la lista son: ")
print(pares)
print("Los numeros impares de la lista son: ")
print(impares)