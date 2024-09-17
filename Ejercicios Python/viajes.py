#Viajes
presup = int(input("Ingrese su presupuesto:"))
costo_Km = 100
distancia = presup / costo_Km
if distancia < 1500 :
    print("No puedes viajar, quedate en casa")
elif distancia <1600 :
    print("Puedes viajar a México :)")
elif distancia < 2400 :
    print("Puedes viajar a P.V")
elif distancia < 3600 :
    print("Puedes viajar va acapulco")
else:
    print("Puedes viajar a Cancún")
