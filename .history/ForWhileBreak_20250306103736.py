libros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
buscaLibro="O Hobbit"
for libro in libros:
    if libro == buscaLibro:
        print(f"Libro encontrado ")
        break
    print(f"****{libro}*******")