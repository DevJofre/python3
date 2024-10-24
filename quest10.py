with open("numeros.txt", "r") as number:

    contador = number.read()

    contador_number = contador.split()

print("Conteudo do arquivo:")
print(contador_number)
