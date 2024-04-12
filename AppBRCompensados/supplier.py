class Supplier:
    def __init__(self):
        self.supplier = {}
    
    def add_supplier(self, name, document, phone, email):
        if document in self.supplier:
            print("\nFornecedor já cadastrado.")
        else:
            self.supplier[document] = {"name":name, "phone":phone, "email":email}

    def del_supplier(self, document):
        if document in self.supplier:
            del self.supplier[document]
            print("\nFornecedor excluído com sucesso.")
        else:
            print("\nFornecedor não localizado na lista de fornecedores.")
        
    def update_supplier(self, name, document, phone, email):
        if document in self.supplier:
            self.supplier[document][name] = name
            self.supplier[document][phone] = phone
            self.supplier[document][email] = email
            print("\nDados do fornecedor atualizado com sucesso.")
        else:
            print("\nFornecedor não localizado.")
    
    def print_suppliers(self):
        print("\nLista de Fornecedores:")
        for document, suppliers in self.supplier.items():
            print(f"\nNome: {suppliers['name']}")
            print(f"CNPJ: {document}")
            print(f"Telefone: {suppliers['phone']}")
            print(f"E-Mail: {suppliers['email']}")
    
    def print_supplier(self, document):
        if document in self.supplier:
            print(f"\nNome: {self.supplier[document]['name']}")
            print(f"CNPJ: {document}")
            print(f"Telefone: {self.supplier[document]['phone']}")
            print(f"E-Mail: {self.supplier[document]['email']}")
        else:
            print("\nFornecedor não Localizado.")