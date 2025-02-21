ingreso=int(input("Ingrese el total de sus gastos del mes: "))
saldo=print(f"tu saldo es de "ingreso-3000)
if ingreso>3000:
    print(f"Atención!!! excediste el limite de lo planificado por {saldo}")
elif ingreso==3000:
    print("Estamos al límite")
else:
 print(f"Estamos dentro de lo planificado tienes {saldo} ")
