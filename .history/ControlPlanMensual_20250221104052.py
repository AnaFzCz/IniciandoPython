ingreso=int(input("Ingrese el total de sus gastos del mes: "))
if ingreso>3000:
    saldo=3000-ingreso
    print("Atención!!! excediste el limite de lo planificado por ",saldo)
elif ingreso==3000:
    print("Estamos al límite")
else:
    saldo=3000-ingreso
    print("Estamos dentro de lo planificado tienes ",saldo )
