# Abrindo e lendo um arquivo de texto
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Escrevendo em um arquivo de texto
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um exemplo de escrita em arquivo.")
