ingreso=int(input("Ingrese el total de sus gastos del mes R$: "))
limite=3000
if ingreso>=limite:
    print(f"Atención!!! excediste el limite de lo planificado ")
elif ingreso==limite:
    print("Estamos al límite")
else:
 print(f"Estamos dentro de lo planificado tienes ")
