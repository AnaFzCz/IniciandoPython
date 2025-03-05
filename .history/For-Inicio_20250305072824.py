# for
nomes = ["Carlos","Ana","Pedro","Maria"]
for nome in nomes:
    print(nome)
# while
contador=0
while contador <5:
    print(f"Contador actual:{contador}")
    contador+=1
# for - break

nomes =["PM3", "Alura","Latam","Otros"]
for nome in nomes:
    if nome =="Alura":
        print("Nome encontrado! Saliendo del lazo")
        break
    print(nome)
    