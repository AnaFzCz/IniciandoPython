ingreso=float(input("Ingresa el monto de tus gastos: "))
limite=3000.0
saldo=ingreso-limite

if ingreso==limite:
    print("estamos al limite, no puedes tener más gastos")
elif ingreso <=limite:
    print(f"Aún contamos con saldo de {saldo}")
else:
    print(f"Excediste el saldo de los planificado por {saldo}")