import re


def valida_ip(ip):

    padrao = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

    if padrao.match(ip):

        octetos = ip.split(".")
        return all(0 <= int(octeto) <= 255 for octeto in octetos)
    return False


ips_validos = []
ips_invalidos = []

with open("ips.txt", "r") as arquivo_entrada:
    for linha in arquivo_entrada:
        ip = linha.strip()
        if valida_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open("relatorio_ips.txt", "w") as arquivo_saida:
    arquivo_saida.write("Endereços IP Válidos:\n")
    for ip in ips_validos:
        arquivo_saida.write(f"{ip}\n")

    arquivo_saida.write("\nEndereços IP Inválidos:\n")
    for ip in ips_invalidos:
        arquivo_saida.write(f"{ip}\n")

print("Relatório de endereços IP gerado em 'relatorio_ips.txt' com sucesso!")
