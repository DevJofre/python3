with open("texto.txt", "r") as arquivo:

    conteudo = arquivo.read()

palavras = conteudo.split()

numero_palavras = len(palavras)

print(f"O arquivo 'texto.txt' contém {numero_palavras} palavra(s).")
