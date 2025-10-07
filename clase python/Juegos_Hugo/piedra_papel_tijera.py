
import random


print("Bienvenido a juegos de Hugo")
selecciona_juego = int(input("Elije uno de los siguientes juegos escribiendo el número correspondiente" \
"\n 1- Adivina el número" \
"\n 2- Pedra - Paper -Tisores" \
"\n 3- El Penjat \n"  \
"Número del juego: "))

#! JUEGO NÚMERO 1
if selecciona_juego == 1:
    print("Tienes que adivinar el número aleatorio entre el 1 y el 10")
    print("Tienes 3 intentos, si fallas los 3 pierdes")
    number = random.randint(1,10)
    # print("Número random es: ", number) #comentar esto al acabar

    first_try = int(input("Dime el primer número: "))

    if first_try > number:
        print("Es mas grande del que buscamos")
    else:
        print("Es mas pequeño del que buscamos")
    if first_try == number:
        print("Felicidades, el numero era: ", number, "has GANADO")
    else:
        print("No es el número: ", first_try)
        second_try = int(input("Dime el segundo número: "))
        if second_try > number:
            print("Es mas grande del que buscamos")
        else:
            print("Es mas pequeño del que buscamos")
        if second_try == number:
            print("Felicidades, el numero era: ", number, "has GANADO")
        else:
            print("No es el número: ", second_try)
            third_attempt = int(input("Dime el tercer y último número: "))
            if third_attempt == number:
                print("Felicidades, el numero era: ", number, "has GANADO")
            else:
                print("No es el número: ", third_attempt)
                print("Has PERDIDO, el número era: ", number)

#! JUEGO NÚMERO 2
elif selecciona_juego == 2:
    print("Juego en mantenimiento")

#! JUEGO NÚMERO 3
elif selecciona_juego == 3:
    print("Juego en mantenimiento")
else:
    print("Error 404: Tienes que elejir un número de juego válido")