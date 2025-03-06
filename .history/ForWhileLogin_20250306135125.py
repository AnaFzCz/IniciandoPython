while True:
    usuario=input("Ingrese su nombre de usuario:")
    contrasena= input("Ingresa su contraseña (números): ")
    if len(usuario) <5:
        print("El nombre del usuario debe tener por lo menos 5 caracteres")
        print("********************")
        continue
    if len(contrasena)<8:
        print("la contraseña debe tener por lo menos 8 caracteres")
        continue
    print (f"Registro realizado con éxito {usuario} - {contrasena}")
    break    