from os import system
control = True #variable de control del bucle 
while control == True:
    print("1. calcular si el numero es primo\n2. Factorial\n3. Salir") #\n es una nueva linea, funciona como un enter
    opcion =int(input("ingrese la opcion:"))
    if opcion  == 1:
        system("cls")
        print("Calcula si el numero es primo")
        Numero = int(input("Ingrese el numero a probar:"))
        cont = 0
        for divisor  in range (1,Numero+1):
            if (Numero % divisor) == 0 :
                cont += 1
            if cont > 2:
                print( f"{Numero} no es primo")
            else:
                print(f"el {Numero} es primo")
    elif opcion == 2:
        system("cls")
        print("Calcula el factorial del numero")
        numero = int(input("Ingrese el numero a probar"))
        fact =1
        for i in range (1,numero+1):
            fact *= i
        print(f"{numero}! = {fact}")
    elif opcion == 3:
        control = False
    else:
        print("opcion no valida")

