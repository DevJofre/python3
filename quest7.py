with open("texto.txt", "r") as arquivo:

    conteudo = arquivo.read()

conteudoMOD = conteudo.replace("mundo", "Python")

with open("modificado.txt", "w") as arquivo_modificado:

    arquivo_modificado.write(conteudoMOD)

print("Conteúdo modificado e escrito em 'modificado.txt' com sucesso!")
