import csv

# Lendo um arquivo CSV
with open("dados.csv", "r") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)

# Escrevendo em um arquivo CSV
dados = [["Nome", "Idade"], ["João", 25], ["Maria", 30]]

with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)
