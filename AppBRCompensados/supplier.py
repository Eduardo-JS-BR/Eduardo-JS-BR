from data import Data
from address import Address

data = Data()
address = Address()

class Supplier:
    def __init__(self) -> None:
        pass
    
    def add_supplier(self):
        name = input("\nNome do Fornecedor: ")
        document = input("CNPJ do Fornecedor: ")
        phone = input("Telefone do Fornecedor: ")
        email = input("E-Mail do Fornecedor: ")

        new_data = {
            "name": name,
            "document": document,
            "phone": phone,
            "email": email
        }

        data.add_data(new_data, "supplier")
        address.add_address(document)
        print("\nFornecedor cadastrado com sucesso.")

    def del_supplier(self):
        document = input("\nDigite o CNPJ do Fornecedor: ")
        data.del_data("supplier", "document", document)
        address.del_address(document)
        print("\nFornecedor Excluído com Sucesso.")
        
    def update_supplier(self):
        name = input("\nNome do Fornecedor: ")
        document = input("CNPJ do Fornecedor: ")
        phone = input("Telefone do Fornecedor: ")
        email = input("E-Mail do Fornecedor: ")
        
        new_data = {
            "name": name,
            "document": document,
            "phone": phone,
            "email": email
        }

        data.update_data("supplier", "document", document, new_data)
        address.update_address(document)
        print("\nDados do Fornecedor Atualizado com Sucesso!")
    
    def print_suppliers(self):
        supplier_data = data.return_class_data_in_json("supplier")

        for supplier in supplier_data:
            print(f"\nNome: {supplier["name"]}")
            print(f"Documento: {supplier["document"]}")
            print(f"Telefone: {supplier["phone"]}")
            print(f"E-Mail: {supplier["email"]}")
            supplier_address = address.return_address(supplier["document"])
            print(f"Endereço: {supplier_address["street"]}")
            print(f"Número: {supplier_address["number"]}")
            print(f"Bairro: {supplier_address["neighborhood"]}")
            print(f"Cidade: {supplier_address["city"]}")
            print(f"Estado: {supplier_address["state"]}")
            print(f"CEP: {supplier_address["zip"]}")
    
    def print_supplier(self):
        document = input("\nDigite o CNPJ do Fornecedor: ")
        supplier_data = data.return_data_in_json("supplier", "document", document)
        supplier_address = address.return_address(document)

        print(f"\nNome: {supplier_data["name"]}")
        print(f"Documento: {supplier_data["document"]}")
        print(f"Telefone: {supplier_data["phone"]}")
        print(f"E-Mail: {supplier_data["email"]}")
        print(f"Endereço: {supplier_address["street"]}")
        print(f"Número: {supplier_address["number"]}")
        print(f"Bairro: {supplier_address["neighborhood"]}")
        print(f"Cidade: {supplier_address["city"]}")
        print(f"Estado: {supplier_address["state"]}")
        print(f"CEP: {supplier_address["zip"]}")