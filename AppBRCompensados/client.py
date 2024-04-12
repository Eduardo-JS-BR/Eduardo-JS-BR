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
            print("\nCliente deletado com sucesso.")
        else:
            print("\nCliente não encontrado na lista de clientes.")

    def update_client(self, name, document, phone, email):
        if document in self.client:
            self.client[document][name] = name
            self.client[document][phone] = phone
            self.client[document][email] = email
            print("\nDados do cliente atualizados com sucesso.")
        else:
            print("\nCliente não localizado.")

    def print_clients(self):
        print("\nLista de Clientes: ")
        for document, clients in self.client.items():
            print(f"\nNome: {clients['name']}")
            print(f"Documento: {document}")
            print(f"Telefone: {clients['phone']}")
            print(f"E-Mail: {clients['email']}")
    
    def print_client(self, document):
        if document in self.client:
            print(f"\nNome: {self.client[document]['name']}")
            print(f"Documento: {document}")
            print(f"Telefone: {self.client[document]['phone']}")
            print(f"E-Mail: {self.client[document]['email']}")
        else:
            print("\nCliente não localizado.")

    def client_search(self, document):
        if document in self.client:
            return f"{document} - {self.client[document]['name']}"
        else:
            return "Cliente não localizado."