'''
import random

aleat_entero = random.randint(5,245)
print(aleat_entero)

aleat_float = random.uniform(0.0,5.0)
print(aleat_float)
'''
#para importar funciones especificas del modulo puedo escribir lo siguiente (digamos que quiero importar solo random.randint y random.uniform)

from random import randint, uniform  
aleat_entero = randint(5,245)
print(aleat_entero)

aleat_float = uniform(0.0,5.0)
print(aleat_float)

#crear una lista de 100 numeros aleatorios enteros
#paso 1crear una lista vacia
edades = []
for numero in range(100):
#paso 2 generar el numero aleatorio
    edad = randint(0,110)
#paso 3 agregamos el numero a la lista
    edades.append(edad)
print(edades)
x = len(edades)
print(x)