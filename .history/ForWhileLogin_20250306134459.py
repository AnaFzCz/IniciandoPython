usuario=input("Ingrese su nombre de usuario:")
contrasena= int(input("Ingresa su conytraseña (números): "))

while len(usuario) >=5:
    print("El nombre del usuario debe tener por lo menos 5 caracteres")
     
    while len(contrasena)>=8:
        print("la contraseña debe tener por lo menos 8 caracteres")
print (f"Registro realixado con éxito {usuario} - {contrasena}")        