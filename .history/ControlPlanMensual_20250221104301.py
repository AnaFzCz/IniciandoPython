ingreso=int(input("Ingrese el total de sus gastos del mes: "))
saldo=print(f"tu saldo es de "ingreso-3000)
if ingreso>3000:
    print("Atención!!! excediste el limite de lo planificado por ",saldo)
elif ingreso==3000:
    print("Estamos al límite")
else:
 print("Estamos dentro de lo planificado tienes ",saldo )
