from address import Address
from client import Client
from product import Product

client = Client()
address = Address()
product = Product()

def main():

    while True:
        print("\nCliente\nEstoque\nSair")
        option = input("Digite uma opção: ")
        
        if (option.lower() == "cliente"): # Área Cliente
            while True:
                print("\nNovo Cliente\nExcluir Cliente\nAtualizar Cliente\nAtualizar Endereço\nLista Clientes\nBuscar Cliente\nVoltar")
                option_client = input("Digite uma opção: ")

                if (option_client.lower() == "novo cliente"): # Cadastrar Novo Cliente
                    name = input("\nNome do Cliente: ")
                    document = input("CPF ou CNPJ do Cliente: ")
                    phone = input("Telefone do Cliente: ")
                    email = input("E-Mail do Cliente: ")
                    print("Dados do Endereço:")
                    street = input("Rua: ")
                    number = input("Número: ")
                    neighborhood = input("Bairro: ")
                    city = input("Cidade: ")
                    state = input("Estado: ")
                    zip = input("CEP: ")

                    client.add_client(name, document, phone, email)
                    address.add_address(document, street, number, neighborhood, city, state, zip)
                    print("\nCliente cadastrado com sucesso.")
                
                elif (option_client.lower() == "excluir cliente"): # Excluir um Cliente
                    document = input("\nCPF ou CNPJ do Cliente: ")
                    client.del_client(document)
                    address.del_address(document)
                
                elif (option_client.lower() == "atualizar cliente"): # Atualizar Dados do Cliente
                    document = input("\nCPF ou CNPJ do Cliente: ")
                    name = input("Nome do Cliente: ")
                    phone = input("Telefone do Cliente: ")
                    email = input("E-Mail do Cliente: ")

                    client.update_client(name, document, phone, email)

                elif (option_client.lower() == "atualizar endereço" or option_client.lower() == "atualizar endereco"): # Atualizar Endereço do Cliente
                    document = input("\nCPF ou CNPJ do Cliente: ")
                    street = input("Rua: ")
                    number = input("Número: ")
                    neighborhood = input("Bairro: ")
                    city = input("Cidade: ")
                    state = input("Estado: ")
                    zip = input("CEP: ")

                    address.update_address(document, street, number, neighborhood, city, state, zip)

                elif (option_client.lower() == "lista clientes"): # Lista Todos os Clientes
                    client.print_clients()
                
                elif (option_client.lower() == "buscar cliente"): # Busca um Cliente
                    document = input("\nCPF ou CNPJ do Cliente: ")
                    client.print_client(document)
                    address.print_address(document)
                
                elif (option_client.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option.lower() == "estoque"):
            while True:
                print("\nAdicionar Estoque\nExcluir Estoque\nLista Estoque\nVoltar")
                option_product = input("Digite uma opção: ")

                if (option_product == "adicionar estoque"): # Adicionar Novo Estoque
                    id = input("\nDigite o código do produto: ")
                    length = input("Digite o comprimento: ")
                    width = input("Digite a largura: ")
                    thickness = input("Digite a espessura: ")
                    type_of_glue = input("Digite o tipo de cola: ")
                    quantity = input("Digite a quantidade: ")

                    product.add_product(id, length, width, thickness, type_of_glue, quantity)

                elif (option_product == "excluir estoque"): # Excluir Estoque
                    id = input("\nDigite o código do produto: ")
                    quantity = input("Digite a quantidade: ")

                    product.del_product(id, quantity)

                elif (option_product == "lista estoque"): # Listar Estoque
                    product.print_product()

                elif (option_product == "voltar"): # Volta pro Menu Principal
                    break
                else:
                    print("\nOpção não disponível.")

        elif (option.lower() == "sair"):
            print("\nSaindo\n")
            break
        else:
            print("\nOpção não disponível.")

if __name__ == "__main__":
    main()