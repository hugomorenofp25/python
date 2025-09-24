
#! OPERADORES
'''
+ --> suma
- -->  resta
* -->  multiplicación
/ -->  division normal que si devuelve decimal
// -->  division normal que no devuelve decimal
% -->  módulo (resto) -->  5 % 2 sería 5 / 2 = 4 --> Faltaría 1 para 5 que es el resto
** -->  exponente (potencia)
'''

print((2 ** 4), (2 * 4.), (2 * 8)) #! El punto en "4." permite pasar un valor int a float
#! El resultado sería (2 ** 4) == 16
#! El resultado sería (2 * 4.) == 8.0
#! El resultado sería (2 ** 4) == 8

print((2 % -4), (2 % 4), (2 **3 ** 2))
#! El resultado sería (2 % -4) == -2
#! El resultado sería (2 % 4) == 2
#! El resultado sería (2 **3 ** 2) == 512

var = 2
var = 3
print(var)
#! El resultado es 3 ya que se reemplaza el contenido de la variable

var = "1"
var = '1'
print(var + var)
#! El resultado es 11 ya que son 2 cadena de texo por que tiene ""

a = 6
b = 3
a /= 2 * b
#! El resultado es 9.0 por que es 6 entre 2 * 3 = 9

x = int(input("Ingresa un número: "))
print(x * "5")
#! Si x es 2 El resultado es 55 por que multiplica 2 por la cadena de texto

