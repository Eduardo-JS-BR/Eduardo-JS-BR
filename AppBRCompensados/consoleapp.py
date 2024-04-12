from address import Address
from client import Client
from product import Product
from sales import Sales
from supplier import Supplier

address = Address()
client = Client()
product = Product()
sales = Sales()
supplier = Supplier()

def main():

    while True:
        print("\nCliente\nFornecedor\nEstoque\nVenda\nSair")
        option = input("Digite uma opção: ")
        
        if (option.lower() == "cliente"): # Área Cliente
            while True:
                print("\nNovo Cliente\nExcluir Cliente\nAtualizar Cliente\nAtualizar Endereço\nListar Clientes\nBuscar Cliente\nVoltar")
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

                elif (option_client.lower() == "listar clientes"): # Lista Todos os Clientes
                    client.print_clients()
                
                elif (option_client.lower() == "buscar cliente"): # Busca um Cliente
                    document = input("\nCPF ou CNPJ do Cliente: ")
                    client.print_client(document)
                    address.print_address(document)
                
                elif (option_client.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option.lower() == "fornecedor"): # Área Fornecedor
            while True:
                print("\nNovo Fornecedor\nExcluir Fornecedor\nAtualizar Fornecedor\nAtualizar Endereço\nListar Fornecedores\nBuscar Fornecedor\nVoltar")
                option_supplier = input("Digite uma opção: ")

                if (option_supplier.lower() == "novo fornecedor"): # Cadastrar Novo Fornecedor
                    name = input("\nNome do Fornecedor: ")
                    document = input("CNPJ do Fornecedor: ")
                    phone = input("Telefone do Fornecedor: ")
                    email = input("E-Mail do Fornecedor: ")
                    print("Dados do Endereço:")
                    street = input("Rua: ")
                    number = input("Número: ")
                    neighborhood = input("Bairro: ")
                    city = input("Cidade: ")
                    state = input("Estado: ")
                    zip = input("CEP: ")

                    supplier.add_supplier(name, document, phone, email)
                    address.add_address(document, street, number, neighborhood, city, state, zip)

                elif (option_supplier.lower() == "excluir fornecedor"): # Exclui um Fornecedor
                    document = input("\nCNPJ do Fornecedor: ")
                    supplier.del_supplier(document)
                    address.del_address(document)
                    
                elif (option_supplier.lower() == "atualizar fornecedor"): # Atualiza Dados do Fornecedor
                    document = input("\nCNPJ do Fornecedor: ")
                    name = input("Nome do Fornecedor: ")
                    phone = input("Telefone do Fornecedor: ")
                    email = input("E-Mail do Fornecedor: ")

                    supplier.update_supplier(name, document, phone, email)

                elif (option_supplier.lower() == "atualizar endereço" or option_supplier.lower() == "atualizar endereco"): # Atualiza Endereço do Fornecedor
                    document = input("\nCNPJ do Fornecedor: ")
                    street = input("Rua: ")
                    number = input("Número: ")
                    neighborhood = input("Bairro: ")
                    city = input("Cidade: ")
                    state = input("Estado: ")
                    zip = input("CEP: ")

                    address.update_address(document, street, number, neighborhood, city, state, zip)

                elif (option_supplier.lower() == "listar fornecedores"): # Lista Todos os Fornecedores
                    supplier.print_suppliers()

                elif (option_supplier.lower() == "buscar fornecedor"): # Busca um Fornecedor
                    document = input("\nCNPJ do Fornecedor: ")
                    supplier.print_supplier(document)
                    address.print_address(document)

                elif (option_supplier.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option.lower() == "estoque"): # Área Estoque
            while True:
                print("\nAdicionar Estoque\nExcluir Estoque\nListar Estoque\nVoltar")
                option_product = input("Digite uma opção: ")

                if (option_product.lower() == "adicionar estoque"): # Adicionar Novo Estoque
                    id = input("\nDigite o código do produto: ")
                    length = input("Digite o comprimento: ")
                    width = input("Digite a largura: ")
                    thickness = input("Digite a espessura: ")
                    type_of_glue = input("Digite o tipo de cola: ")
                    quantity = input("Digite a quantidade: ")

                    product.add_product(id, length, width, thickness, type_of_glue, int(quantity))

                elif (option_product.lower() == "excluir estoque"): # Excluir Estoque
                    id = input("\nDigite o código do produto: ")
                    quantity = input("Digite a quantidade: ")

                    product.del_product(id, int(quantity))

                elif (option_product.lower() == "listar estoque"): # Listar Estoque
                    product.print_product()

                elif (option_product.lower() == "voltar"): # Volta pro Menu Principal
                    break
                else:
                    print("\nOpção não disponível.")

        elif (option.lower() == "venda"): # Área Venda
            while True:
                print("\nNova Venda\nExcluir Venda\nEditar Venda\nVoltar")
                option_sales = input("Digite uma opção: ")

                if (option_sales.lower() == "nova venda"): # Adicionar Nova Venda
                    id = input("\nDigite o número da venda: ")
                    document = input("Digite o CPF ou CNPJ do cliente: ")
                    product = input("Digite o código do produto: ")
                    quantity = input("Digite a quantidade: ")
                    type_of_payment = input("Digite o tipo de pagamento: ")
                    total_value = input("Digite o valor total: ")

                    sales.add_sales(id, document, product, int(quantity), type_of_payment, total_value)

                elif (option_sales.lower() == "excluir venda"): # Excluir uma Venda
                    id = input("\nDigite o número da venda: ")

                    sales.del_sales(id)

                elif (option_sales.lower() == "editar venda"): # Edita uma Venda
                    id = input("\nDigite o número da venda: ")
                    document = input("Digite o CPF ou CNPJ do cliente: ")
                    product = input("Digite o código do produto: ")
                    quantity = input("Digite a quantidade: ")
                    type_of_payment = input("Digite o tipo de pagamento: ")
                    total_value = input("Digite o valor total: ")

                    sales.update_sales(id, document, product, int(quantity), type_of_payment, total_value)

                elif (option_sales.lower() == "voltar"): # Volta pro Menu Principal
                    break
                elif (option_sales.lower() == "print"): # Temporário
                    sales.print("123")
                else:
                    print("\nOpção não disponível.")

        elif (option.lower() == "sair"):
            print("\nSaindo\n")
            break
        else:
            print("\nOpção não disponível.")

if __name__ == "__main__":
    main()