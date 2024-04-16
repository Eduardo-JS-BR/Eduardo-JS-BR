from data import Data

data = Data()

class Finance:
    def __init__(self) -> None:
        pass

    def print_sales(self):
        sales_data = data.return_class_data_in_json("sales")

        if (sales_data != None):
            print("\n")
            for sales in sales_data:
                print(f"Venda: {sales["id"]}, Cliente: {sales["name"]}, Valor: R${sales["total_value"]}")
        else:
            print("\nNenhuma Venda Cadastrada.")

    def print_purchases(self):
        purchase_data = data.return_class_data_in_json("purchase")

        if (purchase_data != None):
            print("\n")
            for purchases in purchase_data:
                print(f"Compra: {purchases["id"]}, Fornecedor: {purchases["name"]}, Valor: R${purchases["total_value"]}")
        else:
            print("\nNenhuma Compra Localizada.")

    def print_balance(self):
        balance = 0.0
        sales_value = 0.0
        purchases_value = 0.0

        sales_data = data.return_class_data_in_json("sales")
        purchase_data = data.return_class_data_in_json("purchase")
        
        if (sales_data != None or purchase_data != None):
            for sales in sales_data:
                balance += sales["total_value"]
                sales_value += sales["total_value"]
            
            for purchases in purchase_data:
                balance -= purchases["total_value"]
                purchases_value += purchases["total_value"]
            
            print("\nBalanço: ")
            print(f"Valor Total de Vendas: R${sales_value}")
            print(f"Valor Total de Compras: R${purchases_value}")
            print(f"\nBalanço: R${balance}")
        else:
            print("\nNão há Dados Para Fazer o Balanço.")