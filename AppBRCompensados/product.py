class Product:
    def __init__(self):
        self.product = {}

    def add_product(self, id, length, width, thickness, type_of_glue, quantity):
        if id in self.product:
            self.product[id]["quantity"] += quantity
            print(f"\nEstoque atualizado para produto com código: {id}.")
        else:
            self.product[id] = {"length":length, "width":width, "thickness":thickness, "type_of_glue":type_of_glue, "quantity":quantity}
            print("\nProduto cadastrado com sucesso.")

    def del_product(self, id, quantity):
        if id not in self.product:
            print(f"\nProduto com Código: {id} não localizado no estoque")
        elif self.product[id]["quantity"] < quantity:
            print(f"\nQuantidade insuficiente no estoque para excluir.")
        else:
            self.product[id]["quantity"] -= quantity
            print(f"\nProduto {self.product[id]['id']} removido do estoque. Quantidade restante: {self.product[id]['quantity']}")

    def print_product(self):
        print("\nEstoque de Produtos:")
        for id, product in self.product.items():
            print(f"Código: {id}")
            print(f"Comprimento: {product['length']}")
            print(f"Largura: {product['width']}")
            print(f"Espessura: {product['thickness']}")
            print(f"Tipo de Cola: {product['type_of_glue']}")
            print(f"Quantidade: {product['quantity']}")