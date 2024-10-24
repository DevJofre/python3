import re


def eliminar_espacos_repetidos(arquivo_entrada, arquivo_saida):

    with open("historia.txt", "r") as entrada:
        linhas = entrada.readlines()

    linhas_processadas = []

    for linha in linhas:

        linha = linha.strip()

        linha = re.sub(r'\s+', ' ', linha)

        if linha:
            linhas_processadas.append(linha)

    with open(arquivo_saida, "w") as saida2:

        for i, linha in enumerate(linhas_processadas):
            saida2.write(linha + "\n")

            if i < len(linhas_processadas) - 1:
                saida2.write("\n")


eliminar_espacos_repetidos("entrada.txt", "saida2.txt")
print("Arquivo processado e salvo como 'saida2.txt'.")
