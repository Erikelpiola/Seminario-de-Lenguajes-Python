#Desarrolla un programa que solicite al usuario que ingrese su edad y luego calcule y
#muestre cuántos años le faltan para alcanzar los 100 años.
edad = int (input("Ingresa tu edad: "))
if edad < 100:
    edadaux=100-edad
    print("Te faltan ",edadaux," años para los 100!!!")
elif edad == 100:
    print("Ya tienes 100 años, felicidades!!!")
else:
    edadaux=edad-100
    print("Cumpliste 100 hace: ",edadaux," años")