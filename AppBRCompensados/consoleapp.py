from client import Client
from product import Product
from sales import Sales
from supplier import Supplier
import os

def main():

    client = Client()
    product = Product()
    sales = Sales()
    supplier = Supplier()

    while True:
        print("\n==================\n")
        print("1 - Cliente\n2 - Fornecedor\n3 - Estoque\n4 - Venda\n5 - Sair")
        option = input("Digite uma opção: ")
        os.system("cls") # Windows
        #os.system("clear") # Mac/Linux

        if (option == "1" or option.lower() == "cliente"): # Área Cliente
            while True:
                print("\n==================\n")
                print("1 - Novo Cliente\n2 - Excluir Cliente\n3 - Atualizar Cliente\n4 - Listar Clientes\n5 - Buscar Cliente\n6 - Voltar")
                option_client = input("Digite uma opção: ")
                os.system("cls") # Windows
                #os.system("clear") # Mac/Linux

                if (option_client == "1" or option_client.lower() == "novo cliente"): # Cadastrar Novo Cliente
                    client.add_client()
                
                elif (option_client == "2" or option_client.lower() == "excluir cliente"): # Excluir um Cliente
                    client.del_client()
                
                elif (option_client == "3" or option_client.lower() == "atualizar cliente"): # Atualizar Dados do Cliente
                    client.update_client()

                elif (option_client == "4" or option_client.lower() == "listar clientes"): # Lista Todos os Clientes
                    client.print_clients()
                
                elif (option_client == "5" or option_client.lower() == "buscar cliente"): # Busca um Cliente
                    client.print_client()
                
                elif (option_client == "6" or option_client.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option == "2" or option.lower() == "fornecedor"): # Área Fornecedor
            while True:
                print("\n==================\n")
                print("1 - Novo Fornecedor\n2 - Excluir Fornecedor\n3 - Atualizar Fornecedor\n4 - Listar Fornecedores\n5 - Buscar Fornecedor\n6 - Voltar")
                option_supplier = input("Digite uma opção: ")
                os.system("cls") # Windows
                #os.system("clear") # Mac/Linux

                if (option_supplier == "1" or option_supplier.lower() == "novo fornecedor"): # Cadastrar Novo Fornecedor
                    supplier.add_supplier()

                elif (option_supplier == "2" or option_supplier.lower() == "excluir fornecedor"): # Exclui um Fornecedor
                    supplier.del_supplier()
                    
                elif (option_supplier == "3" or option_supplier.lower() == "atualizar fornecedor"): # Atualiza Dados do Fornecedor
                    supplier.update_supplier()

                elif (option_supplier == "4" or option_supplier.lower() == "listar fornecedores"): # Lista Todos os Fornecedores
                    supplier.print_suppliers()

                elif (option_supplier == "5" or option_supplier.lower() == "buscar fornecedor"): # Busca um Fornecedor
                    supplier.print_supplier()

                elif (option_supplier == "6" or option_supplier.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option == "3" or option.lower() == "estoque"): # Área Estoque
            while True:
                print("\n==================\n")
                print("1 - Adicionar Estoque\n2 - Excluir Estoque\n3 - Listar Estoque\n4 - Atualizar Estoque\n5 - Voltar")
                option_product = input("Digite uma opção: ")
                os.system("cls") # Windows
                #os.system("clear") # Mac/Linux

                if (option_product == "1" or option_product.lower() == "adicionar estoque"): # Adicionar Novo Estoque
                    product.add_product()

                elif (option_product == "2" or option_product.lower() == "excluir estoque"): # Excluir Estoque
                    product.del_product()

                elif (option_product == "3" or option_product.lower() == "listar estoque"): # Listar Estoque
                    product.print_products()
                
                elif (option_product == "4" or option_product.lower() == "atualizar estoque"): # Atualizar Estoque
                    product.update_product()

                elif (option_product == "5" or option_product.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option == "4" or option.lower() == "venda"): # Área Venda
            while True:
                print("\n==================\n")
                print("1 - Nova Venda\n2 - Excluir Venda\n3 - Listar Vendas\n4 - Atualizar Venda\n5 - Voltar")
                option_sales = input("Digite uma opção: ")
                os.system("cls") # Windows
                #os.system("clear") # Mac/Linux

                if (option_sales == "1" or option_sales.lower() == "nova venda"): # Adicionar Nova Venda
                    sales.add_sales()

                elif (option_sales == "2" or option_sales.lower() == "excluir venda"): # Excluir uma Venda
                    sales.del_sales()

                elif (option_sales == "3" or option_sales.lower() == "listar vendas"): # Edita uma Venda
                    sales.print_sales()
                
                elif (option_sales == "4" or option_sales.lower() == "atualizar venda"): # Edita uma Venda
                    sales.update_sales()

                elif (option_sales == "5" or option_sales.lower() == "voltar"): # Volta pro Menu Principal
                    break

                else:
                    print("\nOpção não disponível.")

        elif (option == "5" or option.lower() == "sair"):
            print("\nSaindo\n")
            break

        else:
            print("\nOpção não disponível.")

if __name__ == "__main__":
    main()