with open("texto.txt", "r") as arquivo_texto:
    conteudo_texto = arquivo_texto.read()

with open("copia_text.txt", "r") as arquivo_copia:
    conteudo_copia = arquivo_copia.read()

conteudo_combinado = conteudo_texto + "\n" + conteudo_copia

with open("combinado.txt", "w") as arquivo_combinado:
    arquivo_combinado.write(conteudo_combinado)

print("Conteúdo combinado e escrito com sucesso em 'combinado.txt'.")
