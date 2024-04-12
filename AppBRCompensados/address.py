class Address:
    def __init__(self):
        self.address = {}

    def add_address(self, document, street, number, neighborhood, city, state, zip):
        if document in self.address:
            print("\nEndereço já cadastrado")
        else:
            self.address[document] = {"street":street, "number":number, "neighborhood":neighborhood, "city":city, "state":state, "zip":zip}

    def del_address(self, document):
        if document in self.address:
            del self.address[document]
        else:
            print("\nEndereço não localizado.")

    def update_address(self, document, street, number, neighborhood, city, state, zip):
        if document in self.address:
            self.address[document][street] = street
            self.address[document][number] = number
            self.address[document][neighborhood] = neighborhood
            self.address[document][city] = city
            self.address[document][state] = state
            self.address[document][zip] = zip
            print("\nEndereço atualizado com sucesso.")
        else:
            print(f"\nEndereço não localizado do usuário.")
    
    def print_address(self, document):
        if document in self.address:
            print(f"Rua: {self.address[document]['street']}")
            print(f"Número: {self.address[document]['number']}")
            print(f"Bairro: {self.address[document]['neighborhood']}")
            print(f"Cidade: {self.address[document]['city']}")
            print(f"Estado: {self.address[document]['state']}")
            print(f"CEP: {self.address[document]['zip']}")
        else:
            print(f"\nEndereço não encontrado.")