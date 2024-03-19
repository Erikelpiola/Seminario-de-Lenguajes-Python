numeros =input ("Ingrese una lista de numeros enteros separados por espacios: ")
numeros = [int (numero) for numero in numeros.split()]
cadena=[]
resultado=""
for numero in numeros:
    if numero % 3 !=0:
        cadena.append(numero)
resultado='-'.join(map(str,cadena))
print("aver: ",resultado)
#explicacion para el futuro:
#el .join lo que hace es añadir el '-' entre diferentes string y unirlos
#obtengo los strings gracias a str,cadena que vuelve string a los numeros
#el map por lo visto cambia string en numeros en toda la lista previo a hacer la union del '-'
#Bastante bueno, me gustó 10/10