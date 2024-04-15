from data import Data

data = Data()

class Product:
    def __init__(self) -> None:
        pass

    def add_product(self):
        id = input("\nDigite o código do produto: ")
        length = input("Digite o comprimento (cm): ")
        width = input("Digite a largura (cm): ")
        thickness = input("Digite a espessura (mm): ")
        type_of_glue = input("Digite o tipo de cola: ")
        quantity = input("Digite a quantidade: ")

        new_data = {
            "id": id,
            "length": int(length),
            "width": int(width),
            "thickness": int(thickness),
            "type_of_glue": type_of_glue,
            "quantity": int(quantity)
        }

        data.add_data(new_data, "product")
        print("\nProduto Cadastrado com Sucesso!")

    def del_product(self):
        id = input("\nDigite o Código do Produto: ")
        data.del_data("product", "id", id)
        print("\nProduto Excluído com Sucesso.")
    
    def update_product(self):
        id = input("\nDigite o código do produto: ")
        length = input("Digite o comprimento (cm): ")
        width = input("Digite a largura (cm): ")
        thickness = input("Digite a espessura (mm): ")
        type_of_glue = input("Digite o tipo de cola: ")
        quantity = input("Digite a quantidade: ")

        new_data = {
            "id": id,
            "length": int(length),
            "width": int(width),
            "thickness": int(thickness),
            "type_of_glue": type_of_glue,
            "quantity": int(quantity)
        }

        data.update_data("product", "id", id, new_data)
        print("\nProduto Atualizado com Sucesso!")

    def print_products(self):
        product_data = data.return_class_data_in_json("product")

        for product in product_data:
            print(f"\nID: {product["id"]}")
            print(f"Comprimento: {product["length"]} cm")
            print(f"Largura: {product["width"]} cm")
            print(f"Espessura: {product["thickness"]} mm")
            print(f"Tipo de Cola: {product["type_of_glue"]}")
            print(f"Quantidade: {product["quantity"]}")