'''
Exercici 4: Suma Fins a un Número

Enunciat:
Demana a l’usuari que introdueixi un número enter positiu.

Utilitza un bucle while per calcular la suma de tots els números des de 1 fins al número introduït (incloent-lo).

Mostra el resultat.

Exemple d’Entrada i Sortida:
Entrada:

Introdueix un número: 4
Sortida:

La suma dels números de 1 fins a 4 és 10.
'''

numero = int(input("Dime un numero entero positivo: "))
i = 1
total = 0

while i <= numero:
    total = total + i 
    i = i + 1

print("Total", total)