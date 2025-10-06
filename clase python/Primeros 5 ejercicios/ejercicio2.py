
'''
Realitza un programa que et mostri el següent menú:
--------------Calculadora Area-----------
1- Triangulo
2- Cuadrado
3- Circunferencia
-------------------------------------------------
En funció de l’opció que esculli l’usuari, et demanarà per pantalla les dades necessàries i et
calcularà l’àrea de la figura seleccionada.
'''

from re import match


eleccion = int(input("Elije unas de las 3 opciones: " \
"\n 1- Triangulo " \
"\n 2- Cuadrado " \
"\n 3- Circunferencia: " \
"\n: "))

if eleccion == 1:
    base = int(input("Dime la base"))
    altura = int(input("Dime la altura"))
    final = base * altura / 2
    print("El área de tu triangulo es" , final)
elif eleccion == 2:
    lado = int(input("Dime la longitud de cm del lado del cuadrado: "))
    final_cuadrado = lado ** 2
    print("El área de tu cuadrado es" , final_cuadrado)
elif eleccion ==3 :
    radio = float(input("Dime el radio de la bola: "))
    finalradio = 3.1416 * (radio ** 2)
    print("El área de tu bola es ", finalradio)

else:
    print("Error, solo puedes elejir 1, 2, 2")