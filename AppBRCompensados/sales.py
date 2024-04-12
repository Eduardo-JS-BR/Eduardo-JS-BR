from client import Client

client = Client()

class Sales:
    def __init__(self):
        self.sales = {}
    
    def add_sales(self, id, document, product, quantity, type_of_payment, total_value):
        if id in self.sales:
            print("\nVenda já cadastrada.")
        else:
            self.sales[id] = {"document":document, "product":product, "quantity":quantity, "type_of_payment":type_of_payment, "total_value":total_value}
    
    def del_sales(self, id):
        if id in self.sales:
            del self.sales[id]
            print("\nVenda excluída com sucesso.")
        else:
            print("\nVenda não localizada.")

    def update_sales(self, id, document, product, quantity, type_of_payment, total_value):
        if id in self.sales:
            self.sales[id][document] = document
            self.sales[id][product] = product
            self.sales[id][quantity] = quantity
            self.sales[id][type_of_payment] = type_of_payment
            self.sales[id][total_value] = total_value
            print("\nDados da venda atualizada com sucesso.")
        else:
            print("\nVenda não localizada.")