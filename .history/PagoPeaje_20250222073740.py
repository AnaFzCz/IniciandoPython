# distancia=int(input("Ingrese la distancia recorrida (km): "))
# var1=10,00
# var2=20,00
# var3=30,00

# if distancia >100 and distancia <=200:
#     print(f"Valor de peaje es de R$: {var2}")
# elif distancia <= 100:
#     print(f"Valor de peaje es de R$: {var1}")
# else:
#     print(f"Valor de peaje es de R$: {var3}")
distancia = float(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    print("Valor do pedágio: R$ 10,00")
elif 100 < distancia <= 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")