with open("texto.txt", "r") as arquivo:

    linhas = arquivo.readlines()

numero_linhas = len(linhas)

print(f"O arquivo 'texto.txt' tem {numero_linhas} linha(s).")
