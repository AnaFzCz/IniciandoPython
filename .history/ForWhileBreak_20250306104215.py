libros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
buscaLibro="Dom Casmurro"
for libro in libros:
    if libro == buscaLibro:
        print(f"libro encontrado: {buscaLibro}")
        break