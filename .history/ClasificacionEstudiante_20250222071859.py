nota1= float(input("Ingrese la primera nota: "))
nota2= float(input("Ingrese la segunda nota: "))
nota3= float(input("Ingrese la tercera nota: "))

media= (nota1+nota2+nota3)/3

if media >=5 and media <=7:
    print(f"Tiene una media de {media:.2f}, RECUPERACIÓN")
elif media<5:
    print(f"Tiene una media de {media:.2f}, REPROBADO")
else:
    print(f"Tiene una media de {media:.2f}, APROBADO")
