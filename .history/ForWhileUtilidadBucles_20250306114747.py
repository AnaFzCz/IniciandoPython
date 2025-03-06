libros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

contador=0

for libro in libros:
    contador+=1
    if libro["estoque"]==0:
        continue
    print(f"{contador}- Libro disponible {libro}")
    
    