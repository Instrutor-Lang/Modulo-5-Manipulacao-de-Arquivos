# Módulo 5: Manipulação de Arquivos

Este módulo tem como objetivo ensinar os alunos a trabalhar com arquivos de texto, CSV e JSON em Python. Os alunos aprenderão a abrir, ler, escrever e manipular arquivos, além de lidar com erros para garantir um gerenciamento seguro dos dados.

---

## 🎯 Objetivo do Módulo
- Aprender a manipular arquivos de texto, CSV e JSON.
- Entender como abrir, ler, escrever e fechar arquivos.
- Dominar o tratamento de erros ao trabalhar com arquivos.
- Aplicar os conceitos em projetos práticos, como um sistema de registro de clientes e um sistema de backup.

---

## 🏗️ Estrutura da Aula

### 1. Revisão Rápida do Módulo 4 (10 minutos)
- Breve revisão de funções, parâmetros, retorno de valores e escopo de variáveis.
- Resolução de dúvidas sobre o Módulo 4.

### 2. Introdução à Manipulação de Arquivos (20 minutos)
- O que são arquivos e por que são importantes?
- Formatos comuns: texto, CSV, JSON.

### 3. Trabalhando com Arquivos de Texto (40 minutos)
- Abrindo e fechando arquivos.
- Lendo e escrevendo em arquivos de texto.

### 4. Trabalhando com Arquivos CSV (30 minutos)
- Lendo e escrevendo arquivos CSV.

### 5. Trabalhando com Arquivos JSON (30 minutos)
- Lendo e escrevendo arquivos JSON.

### 6. Gerenciamento de Erros ao Manipular Arquivos (20 minutos)
- Tratamento de exceções ao trabalhar com arquivos.

### 7. Atividade Prática (40 minutos)
- Criar um sistema de registro e consulta de clientes usando JSON.

### 8. Desafio Extra (20 minutos)
- Criar um sistema de backup automático.

---

## 📂 Exemplos de Código

### 1. Trabalhando com Arquivos de Texto
**Arquivo:** `arquivos_texto.py`
```python
# Abrindo e lendo um arquivo de texto
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Escrevendo em um arquivo de texto
with open("exemplo.txt", "w") as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Este é um exemplo de escrita em arquivo.")
```

### 2. Trabalhando com Arquivos CSV
**Arquivo:** `arquivos_csv.py`
```python
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
```

### 3. Trabalhando com Arquivos JSON
**Arquivo:** `arquivos_json.py`
```python
import json

# Lendo um arquivo JSON
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)
    print(dados)

# Escrevendo em um arquivo JSON
dados = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)
```

### 4. Gerenciamento de Erros ao Manipular Arquivos
**Arquivo:** `tratamento_erros.py`
```python
try:
    with open("arquivo_inexistente.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
```

### 5. Atividade Prática: Sistema de Registro de Clientes
**Arquivo:** `sistema_clientes.py`
```python
import json

def carregar_dados():
    try:
        with open("clientes.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(clientes):
    with open("clientes.json", "w") as arquivo:
        json.dump(clientes, arquivo, indent=4)

def adicionar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    clientes.append({"nome": nome, "email": email})
    salvar_dados(clientes)
    print("Cliente adicionado com sucesso!")

def listar_clientes(clientes):
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}, Email: {cliente['email']}")

def main():
    clientes = carregar_dados()

    while True:
        print("\nMenu:")
        print("1 - Adicionar cliente")
        print("2 - Listar clientes")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_cliente(clientes)
        elif opcao == '2':
            listar_clientes(clientes)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
```

### 6. Desafio Extra: Sistema de Backup Automático
**Arquivo:** `sistema_backup.py`
```python
import os
import shutil

def fazer_backup(pasta_origem, pasta_destino):
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    for arquivo in os.listdir(pasta_origem):
        origem = os.path.join(pasta_origem, arquivo)
        destino = os.path.join(pasta_destino, arquivo)
        shutil.copy(origem, destino)
        print(f"Copiado: {arquivo}")

fazer_backup("pasta_origem", "pasta_destino")
```

---

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Pronto! Agora você tem o **README.md** explicando o módulo e, em seguida, **apenas os códigos** separados por tópicos. Se precisar de mais ajustes, é só avisar! 😊
