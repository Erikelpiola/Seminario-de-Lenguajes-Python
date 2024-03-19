numeros = input ("Ingrese una lista de numeros enteros separados por espacios: ")
numeros = [int (numero) for numero in numeros.split()]
print("Entre los numeros dados, si se encuentra uno negativo, se detiene la impresion: ")
for numero in numeros:
    if numero < 0:
        break
    print(numero)