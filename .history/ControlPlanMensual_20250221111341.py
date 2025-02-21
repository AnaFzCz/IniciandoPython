ingreso=float(input("Ingresa el monto de tus gastos: "))
limite=3000.0
saldo=limite-ingreso
if ingreso>limite:
   print(f"Excediste el limite de lo planificado por {saldo}, oh no!!!")
else:
   print(f"Aún estamos dentro de nuestro plan, tenemos un saldo de {saldo}")