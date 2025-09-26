
#! TIPOS DE VARIABLES

'''
Las variables siempre han de ser en minúsculas y separadas por _
'''
# Esto es una variable string --> de texto
my_variable = "Mi variable String"
print(my_variable) 

# Esto es una variable int --> de números
my_int = 5
print(my_int)

my_int_to_str_variable = str(my_int) # Pasamos el int de antes a string
print(my_int_to_str_variable) #Imprime lo mismo 5 pero un 5 de texto
print(type(my_int_to_str_variable)) # Nos dice que efectivamenet es tring la variable

# Esto es una variable bool --> un booleano (True o False)
my_bool = True
print(my_bool)

# Aquí estamos imprimiendo "Mi variable String 5 True
print(my_variable, my_int, my_bool)
print("Este es el valor de:", my_bool)

#! Algunas funciones del sistema
print(len(my_variable)) # Cuenta los carácteres que contenga la variable

# Variables en una sola línea. (No usar esta práctica mucho)
name, surname, alias, age = "Hugo", "Moreno", "hugomontaña", 20
print("Me llamo: " , name, surname, ". Mi edad es:" , age, ". Y mi alias es:" , alias)

nombre = input("Cual es tu nombre: ")
años = input("Que edad tienes: ")
print("Te llamas", nombre , "y tienes", años, "anos")