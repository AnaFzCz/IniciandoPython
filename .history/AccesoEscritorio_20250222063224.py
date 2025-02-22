ingresoHora=int(input("Ingrese la hora actual (formato 24 horas): "))

if ingresoHora > 8 and ingresoHora < 18:
    print("Accesso permitido")
else:
    print("Acceso negado")