#Menú de operaciones básicas
print("S. Sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nT. Residuo")
Opción = input("Ingrese la opción deseada:")
Opción = Opción.upper()
#Necesitamos configurarlo para que en caso de que el usuario ingrese una letra diferente de las opciones, el programa no haga nada
if Opción not in ["s","R","M","D","T"]:
    print("Opcion no valida ._.")
else:
    numero1 = float(input("Ingrese el primer valor:"))
    numero2 = float(input("Ingrese el segundo valor:"))
    if Opción == "S" :
        resultado = numero1 + numero2
    elif Opción == "R" :
        resultado = numero1 - numero2
    elif Opción == "M" :
        resultado = numero1 * numero2
    elif Opción == "D" :
        resultado = numero1 / numero2
    elif Opción == "T" :
        resultado = numero1 % numero2
    else:
        print("._.") 
    print(f"el resultado es:{resultado}")