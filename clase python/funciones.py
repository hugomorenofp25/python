
#! Funciones

def operaciones(num1,num2):
    resSuma = suma(num1,num2)
    resResta = resta(num1,num2)
    return resSuma, resResta


def suma(num1,num2):
    res = num1+num2
    return res;

def resta(num1,num2):
    res = num1-num2
    return res;


num3 = 5
print(suma(7,num3))


def modificarUltimoValor(lista):
    lista[-1] = 0

notas = [7,6,9,5]
modificarUltimoValor(notas)

def modificaValor(numero):
    res = numero -5
num=10
modificaValor(num)
print(num)