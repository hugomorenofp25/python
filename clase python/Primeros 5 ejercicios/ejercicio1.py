
'''
Crea un programa que l’usuari t’introdueixi per pantalla una població y una temperatura, i el
programa et mostri el següent menú:
--------------------------------------------------------
1- Transforma a Kelvin
2- Transforma a Fahrenheit
------------------------------------------------------
En funció de l’opció que esculli l’usuari, mostrarà un resultat o l’altre.
'''

pueblo = input("Dime pueblo: ")
temperatura = int(input("Dime temperaratura: "))

eleccion = int(input("Elije Kelvin (1) o Fahrenheit (2)"))

if eleccion == 1:
    finalkelvin = temperatura + 459.67 / 1.8
    print("Temperatura Kelvin" , finalkelvin)
elif eleccion == 2:
    finalfahrenheit = temperatura * 9 / 5 + 32
    print("Temperatura Fahrenheit" , finalfahrenheit)
else:
    print("Error, Hay que poner 1 o 2")