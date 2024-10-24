def formatar_espaco(espaco):
    return f"{espaco / (1024 * 1024):.2f} MB"


def calcular_porcentagem(espaco, total):
    return (espaco / total) * 100 if total > 0 else 0


usuarios = {}

with open("usuarios.txt", "r") as arquivo:
    for linha in arquivo:

        nome, espaco = linha.split()

        usuarios[nome] = int(espaco)

espaco_total = sum(usuarios.values())

relatorio = []

for i, (usuario, espaco) in enumerate(usuarios.items(), start=1):
    espaco_mb = formatar_espaco(espaco)
    porcentagem = calcular_porcentagem(espaco, espaco_total)
    relatorio.append(f"{i} {usuario:<15} {espaco_mb:<10} {porcentagem:.2f}%")

espaco_medio = espaco_total / len(usuarios) if usuarios else 0
5

with open("relatorio.txt", "w") as arquivo_saida:
    arquivo_saida.write("Disciplina: Algoritmos e Programação II\n")
    arquivo_saida.write(
        "Professor: Paulo César Fernandes de Oliveira, BSc, PhD\n\n")
    arquivo_saida.write("ACME Inc. Uso do espaço em disco pelos usuários\n")
    arquivo_saida.write(
        "------------------------------------------------------------------------\n")
    arquivo_saida.write("Nr. Usuário      Espaço utilizado % do uso\n")

    for linha in relatorio:
        arquivo_saida.write(f"{linha}\n")

    arquivo_saida.write(f"Espaço total ocupado: {
                        formatar_espaco(espaco_total)}\n")
    arquivo_saida.write(f"Espaço médio ocupado: {
                        formatar_espaco(espaco_medio)}\n")

print("Relatório gerado em 'relatorio.txt' com sucesso!")
