cuentaRegresiva= int(input("ingrese el número entero: "))
for contador in  range(cuentaRegresiva,0,-1):
 if contador%2==0:
    print(f"Faltan apenas num {contador}. No pierda está oportunidad")
    contador-=1
 else:
    print(f"El conteo continua {contador} segundos restantes")
print("Aproveche la promoción ahora!!!")    