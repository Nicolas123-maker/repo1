#Función que recibe cantidad de datos float, rango de valores y retorna una lista
#Funcion que recibe una lista y calcula el promedio y la desviacion estandar
#Funcion que calcula cuantos datos estan por encima del promedio en una lista y cuales son esos datos

from random import uniform #para generar aleatorios tipo float
#Funcion 1
from math import sqrt #Funcion para la raiz cuadrada
from random import randint #aleatrorio para enteros
def crea_lista_float(cantidad: int, limite_inf: float, lim_sup: float) : #con el :float le estamos diciendo a la funcion que tipo de dato va arecibir y que tipo de dato esperamos que nos devuelva
    #1. creo una lista vacia 
    aleatorios_float = []
    #2. Utilizo un bucle
    for i in range(cantidad) :
        #3. genero el numero aleatorio
        numero = uniform(limite_inf, lim_sup)
        #4. Agrego el numero a la lista
        aleatorios_float.append(numero)
    return aleatorios_float
#Funcion 2
def estadisticas(datos: list):
    promedio = sum(datos) /len(datos)
    suma = 0
    for xi in datos:
        suma += (xi - promedio)**2
    interior_de_la_raiz  = suma/ len(datos)
    Desviacion = sqrt(interior_de_la_raiz)
    return promedio, Desviacion
#Funcion 3
def datos_encima_prom(lista: list, promedio: float):
    list = []
    contador = 0
    for i in lista:
        if i > promedio:
            contador += 1
            list.append(i)
    return contador, list 

#+++++++++++
#programa principal
#+++++++++

#invocamos a la funcion 1
lista_aleatorios = crea_lista_float(22,0.1,5.0) #asignamos la funcion a una variable en el programa
print(lista_aleatorios)

#invocamos funcion 2
variable1, variable2 = estadisticas(lista_aleatorios)
print(f"el promedio es {variable1}, la desviacion es {variable2} ")

#invocamos funcion 3
cont, lis = datos_encima_prom(lista_aleatorios, variable1)
print(f"hay {cont} valores mayores que el pormedio. estos son los datos {lis}")