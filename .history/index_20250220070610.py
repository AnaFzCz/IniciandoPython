

        
    edad = int(input("Indique su edad:"))
    documento = input("Tiene documento?(si/no):")
    
    if edad >= 18 and documento == "si":
        print("Entrada permitida!!")
        
    else:
        print("Entrada negada")