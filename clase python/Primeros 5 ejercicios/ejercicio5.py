'''
Exercici 5: Nombre Parell o Senar

Enunciat:
Demana a l’usuari dos números: un inici i un final.

Utilitza un bucle for per recórrer els números dins d’aquest rang (inclosos).

Mostra cada número amb una indicació de si és parell o senar.

Exemple d’Entrada i Sortida:
Entrada:

Introdueix el número inicial: 3
Introdueix el número final: 7
Sortida:

3 és senar.
4 és parell.
5 és senar.
6 és parell.
7 és senar.
'''
print("Dime 2 números de entrada y salida")
num_entrada = int(input("Numero de entrada: "))
num_salida = int(input("Numero de entrada: "))

num_salida = num_salida + 1
i = num_entrada

for i in range(num_entrada, num_salida):
    if i % 2 == 0:
        print(i, "Es parell")
    else:
        print(i, "Es senar")