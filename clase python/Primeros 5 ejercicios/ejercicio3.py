'''
Exercici 3: Taula de Multiplicar
Demana a l’usuari que introdueixi un número enter.

Utilitza un bucle for per generar la seva taula de multiplicar des de 1 fins a 10.
Mostra el resultat en el format següent:

n × 1 = resultat
n × 2 = resultat

Exemple d’Entrada i Sortida:
Entrada:

Introdueix un número: 5
Sortida:
5 × 1 = 5
5 × 2 = 10
5 × 3 = 15
...
5 × 10 = 50
'''

numero = int(input("Dime un numero para saber su tabla de multiplicar: "))

for gia in range(1, 11):
    total = gia * numero
    print(numero, " x " , gia, " = ", total)
    
