ingreso=int(input("Ingrese el total de sus gastos del mes R$: "))


if ingreso>3000:
    print(f"Atención!!! excediste el limite de lo planificado ")
elif ingreso==3000:
    print("Estamos al límite")
else:
 print(f"Estamos dentro de lo planificado tienes ")
