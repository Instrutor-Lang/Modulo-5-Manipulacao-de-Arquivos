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
