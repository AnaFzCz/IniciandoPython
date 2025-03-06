cuentaRegresiva= int(input("Ingrese el número entero: "))
for contador in  range(cuentaRegresiva,0,-1):
 if contador%2==0:
    print(f"Faltan apenas num {contador}. No pierda está oportunidad")
 else:
    print(f"El conteo continua {contador} segundos restantes")
print("Aproveche la promoción ahora!!!")    