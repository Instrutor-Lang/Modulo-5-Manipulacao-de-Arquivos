import json

# Lendo um arquivo JSON
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)

# Escrevendo em um arquivo JSON
dados = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
