Matriz = [[1,4,6,8,3],[8,9,12,54,47],[98,45,78,3,10]]
print(Matriz[2][2]) #Le indico la posicion dentro de la matriz del dato que quiero imprimir, en este caso el numero 78, que esta en fila 2 columna 2
#Con la matriz puedo hacer operaciones matematicas para cambiar el valor de un dato dentro de la matriz, teniendo tambien en cuenta que las listas son objetos iterables y que les puedo cambiar el valor de sus elementos
Matriz [2][4] = 50 #Con esto cambio el 10 de la fila 2 por un 50

print(Matriz[1])#Con esto puedo imprimir toda la fila 1 de la matriz

#Generar los indices para recorrer la matriz, con esto entre otras cosas puedo multiplicar toda la matriz por una constante
for i in range(3):#para las filas
    for j in range(5):#para las columnas
        print(f"fila {i} columna {j}")

#Ahora hagamos el bucle para el escalar
for i in range(3):
    for j in range(5):
        Matriz [i][j] = Matriz [i][j] * 2
print (Matriz)