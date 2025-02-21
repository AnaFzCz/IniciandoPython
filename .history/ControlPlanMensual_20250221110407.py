ingreso=float(input("Ingresa el monto de tus gastos: "))
limite=3000.0


if ingreso>limite:
   print("estamos al limite, no puedes tener más gastos")
else:
    saldo=ingreso-limite
    print(f"Excediste el saldo de los planificado por {saldo}")