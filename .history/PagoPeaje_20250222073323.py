distancia=int(input("Ingrese la distancia recorrida (km): "))
var1=10,00
var2=20,00
var3=30,00

if distancia >100 and distancia <=200:
    print(f"Valor de peaje es de: {var1}")
elif distancia <= 100:
    print(f"Valor de peaje es de: {var2}")
else:
    print(f"Valor de peaje es de: {var3}")