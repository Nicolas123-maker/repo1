lista = [4,5,4,8,33,22,66,55,44,77,88,99,1100000,20000,5]
acum = 0
n_elem = len(lista)
cont = 0
while cont < n_elem:
    acum += lista[cont]
    cont += 1
print (f"la suma es {acum} y debe dar {sum(lista)}")
