peso= float(input("Ingrese su peso (Kg) "))
altura=float(input("Ingresa tu altura (m) "))
imc=peso/(altura**2) 
print(f"Tu IMC es de {imc}")
if imc<18.5:
    print("Tu peso es bajo")
elif imc<25:
    print("Tu peso es normal")
else:
    print("Tu peso está por encima")