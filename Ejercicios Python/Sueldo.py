#Sueldo
Horas = int(input("Horas:"))
Valor_Hora = int(input("Valor_Hora:"))
Total = 0
if Horas > 50 or Horas < 0:
    print("Numero de horas no permitido")
elif Horas > 45:
    Total = (Valor_Hora*40) + (Valor_Hora*2*5) + (Valor_Hora*3*(Horas-45))
elif Horas > 40:
    Total = (Valor_Hora*40) + (Valor_Hora*2*(Horas-40))
else:
    Total = (Valor_Hora*Horas)
print(f"Total a pagar ${Total}") 