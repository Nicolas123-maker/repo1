

from random import randint
filas=4
columnas=13
Lista = []               
for i in range(filas):      
    Lista.append([])      
    for j in range(columnas):    
        n = randint(1,100)
        Lista[i].append(n)  

print(Lista)
