from data import Data

data = Data()

class Sales:
    def __init__(self) -> None:
        pass
    
    def add_sales(self):
        id = input("\nDigite o número da venda: ")
        document = input("Digite o CPF ou CNPJ do cliente: ")
        product = input("Digite o código do produto: ")
        quantity = input("Digite a quantidade: ")
        type_of_payment = input("Digite o tipo de pagamento: ")
        total_value = input("Digite o valor total: ")

        new_data = {
            "id": id,
            "document": document,
            "product": product,
            "quantity": int(quantity),
            "type_of_payment": type_of_payment,
            "total_value": float(total_value)
        }

        data.add_data(new_data, "sales")
        print("\nVenda Cadastrada como Sucesso!")
    
    def del_sales(self):
        id = input("\nDigite o Código da Venda: ")
        data.del_data("sales", "id", id)
        print("\nVenda Excluída com Sucesso.")
    
    def update_sales(self):
        id = input("\nDigite o número da venda: ")
        document = input("Digite o CPF ou CNPJ do cliente: ")
        product = input("Digite o código do produto: ")
        quantity = input("Digite a quantidade: ")
        type_of_payment = input("Digite o tipo de pagamento: ")
        total_value = input("Digite o valor total: ")

        new_data = {
            "id": id,
            "document": document,
            "product": product,
            "quantity": int(quantity),
            "type_of_payment": type_of_payment,
            "total_value": float(total_value)
        }

        data.update_data("sales", "id", id, new_data)
        print("\nVenda Atualizada como Sucesso!")

    def print_sales(self):
        sales_data = data.return_class_data_in_json("sales")

        for sales in sales_data:
            print(f"\nID: {sales["id"]}")
            print(f"Cliente: {sales["document"]}")
            print(f"Produto: {sales["product"]}")
            print(f"Quantidade: {sales["quantity"]}")
            print(f"Tipo de Pagamento: {sales["type_of_payment"]}")
            print(f"Valor Total: {sales["total_value"]}")