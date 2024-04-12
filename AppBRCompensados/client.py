class Client:
    def __init__(self):
        self.client = {}
    
    def add_client(self, name, document, phone, email):
        if document in self.client:
            print("\nCliente já cadastrado.")
        else:
            self.client[document] = {"name":name, "phone":phone, "email":email}

    def del_client(self, document):
        if document in self.client:
            del self.client[document]
            print(f"\nCliente {document} deletado com sucesso.")
        else:
            print(f"\nCliente com o CPF {document} não encontrado na lista de clientes.")

    def update_client(self, name, document, phone, email):
        if document in self.client:
            self.client[document][name] = name
            self.client[document][phone] = phone
            self.client[document][email] = email
            print(f"\nDados do cliente com CPF {document} atualizados com sucesso.")
        else:
            print(f"\nCliente não localizado com o CPF {document}")

    def print_clients(self):
        print("\nLista de Clientes: ")
        for document, clients in self.client.items():
            print(f"Nome: {clients['name']}")
            print(f"Documento: {document}")
            print(f"Telefone: {clients['phone']}")
            print(f"E-Mail: {clients['email']}")
    
    def print_client(self, document):
        if document in self.client:
            print(f"\nNome: {self.client[document]['name']}")
            print(f"Documento: {document}")
            print(f"Telefone: {self.client[document]['phone']}")
            print(f"E-Mail: {self.client[document]['email']}")