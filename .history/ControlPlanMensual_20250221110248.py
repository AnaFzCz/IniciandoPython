ingreso=float(input("Ingresa el monto de tus gastos: "))
limite=3000.0
# saldo=ingreso-limite

if ingreso>limite:
    print("estamos al limite, no puedes tener más gastos")
else:
    print("Excediste el saldo de los planificado ")