# Apuntes 22-09-2025
textolargo = "Me llamo Hugo, estoy en clase de Ce"
len(textolargo)
print(textolargo.upper()) # Poner el texto de la variable en Mayusculas
print(textolargo.find("Ce")) # Decir en que posicion está "Ce"
textolargo = textolargo + " y es Lunes"
print(textolargo)


''' Ejercicio de preguntar la edad y si es mas pequeño de 16
    no puede trabajar, si es mayor si puedes trabajar,
    si es mayor de 67 que diga que te toca juvilarte y 
    si es justo 67 que te diga, es tu último año 
'''

edad = int(input("Indicame tu edad: "))
if edad <= 16:
    print("No puedes trabajar")
elif edad > 67:
    print("Te toca Juvilarte")
elif edad == 67:
    print("Tienes 67 años")
else:
    print("Si puedes trabajar")

# Otro ejercicio
baja = True
edad = int(input("Indicame tu edad: "))

if edad > 16 and baja != True:
    print("Puedes currar")
else:
    print("No puedes trabajar")

'''Ejercicio de preguntar al usuario si está de baja o no,
    convierte su respuesta en un booleano y haz las condiciones
    de que indiquen si se puede trabajar: edad entre 67 y 16
    y no estar de baja
'''

baja = (input("Estas de baja? Si/No: "))
baja = baja.lower()

if baja == "si":
    baja = True
elif baja == "no":
    baja = False
else:
    print("Respuesta incorrecta")

#Ahora preguntamos la edad
edad = int(input("Introduce tu edad: "))

if edad < 67 and baja > 16 and baja == False:
    print("Puedes trabajar")
else:
    print("No puedes trabajar")

print(type(baja))