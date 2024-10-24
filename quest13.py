def paginar_arquivo(arquivo_entrada, arquivo_saida):

    with open("historia.txt", "r") as entrada:
        linhas = entrada.readlines()

    max_linhas_por_pagina = 60
    max_caracteres_por_linha = 76
    pagina_atual = 1
    linhas_na_pagina = []

    with open(arquivo_saida, "w") as saida:
        for linha in linhas:

            linha = linha.strip()

            while len(linha) > max_caracteres_por_linha:
                saida.write(linha[:max_caracteres_por_linha] + "\n")
                linha = linha[max_caracteres_por_linha:]

            if linha:
                linhas_na_pagina.append(linha)

            if len(linhas_na_pagina) == max_linhas_por_pagina:
                for l in linhas_na_pagina:
                    saida.write(l + "\n")
                saida.write(f"Página {pagina_atual} - {arquivo_entrada}\n\n")
                pagina_atual += 1
                linhas_na_pagina.clear()

        if linhas_na_pagina:
            for l in linhas_na_pagina:
                saida.write(l + "\n")
            saida.write(f"Página {pagina_atual} - {arquivo_entrada}\n\n")


paginar_arquivo("entrada.txt", "saida.txt")
print("Arquivo paginado gerado com sucesso em 'saida.txt'.")
