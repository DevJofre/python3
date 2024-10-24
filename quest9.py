with open("texto.txt", "r") as arquivo:

    conteudo = arquivo.read()

numero_letras = len(conteudo.replace(" ", ""))

print(f"O arquivo 'texto.txt' contém {numero_letras} letra(s).")
