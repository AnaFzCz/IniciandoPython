ingreso=int(input("Ingrese el total de sus gastos del mes R$: "))
saldo=3000-ingreso
print(f"tu saldo es de {saldo}")

if ingreso>3000:
    print(f"Atención!!! excediste el limite de lo planificado por {saldo}")
elif ingreso==3000:
    print("Estamos al límite")
else:
 print(f"Estamos dentro de lo planificado tienes {saldo} ")
