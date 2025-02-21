manzanas= int(input("Cuántas manzanas vendiste hoy: "))
bananas= int(input("Cuántas bananas vendiste hoy: "))
if manzanas == bananas:
    print("Vendiste la misma cantidad de manzanas y bananas")
elif manzanas>bananas:
    print("vendiste más manzanas")
else:
    print("vendiste más bananas")