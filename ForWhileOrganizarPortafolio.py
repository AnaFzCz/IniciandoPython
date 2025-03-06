projectos=["website","jogo","análisis de datos", None, "Aplicativo Móvil"]

for projecto in projectos: #for projecto is None
    if projecto == None:
        print("Proyecto ausente")
    else:
        print(f"* {projecto}")
        