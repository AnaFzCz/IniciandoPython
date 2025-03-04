rentaMensual= int(input("Ingrese el valor de su renta mensual: "))
parcela= int(input("Ingrese el valor de su parcela deseada: "))

calculo= (rentaMensual * 30)/100

if rentaMensual > 2000 and parcela <= calculo:
    print("Prestado aprobado: la parcela está por debajo del 30 de renta")
else:
    print("Prestado regado: la parcela está por encima del 30 de renta")