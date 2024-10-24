with open("texto.txt", "r") as arquivo_origem:

    conteudo = arquivo_origem.read()

with open("copia_text.txt", "w") as arquivo_copia:

    arquivo_copia.write(conteudo)

print("Conteúdo copiado com sucesso para 'copia_text.txt'.")
