Aviones = ["A320", "Gavilan", "f22", "f35"]
cont = 1
for avion in Aviones:
    print(f"avion{cont} --> {avion}")
    cont= cont + 1
    
#Veamos la diferencia con el while...
indice = 0
cont = len(Aviones) #calcula el numero de elementos de la lista
while indice < cont:
    print(f"avion {indice+1} --> {Aviones[indice]}")
    #Indice = indice + 1
    indice += 1 
#Pedir al usuario una frase y leer cuantas "a" tiene
frase = input("Ingrese una frase:")
cont = 0
for Letra in frase:
    if Letra == "a" :
      cont += 1
print(f"La frase tiene{cont}letras a")


