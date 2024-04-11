from address import Address

class Client:
    def __init__(self, name, document, phone, email, address):
        self.name = name
        self.document = document
        self.phone = phone
        self.email = email
        self.address = address

    def ChangeClientData(self, name, document, phone, email):
        self.name = name if self.name != name else self.name
        self.document = document if self.document != document else self.document
        self.phone = phone if self.phone != phone else self.phone
        self.email = email if self.email != email else self.email

    def PrintClient(self):
        print(f"Cliente: {self.name}\nDocumento: {self.document}\nTelefone: {self.phone}\nE-Mail: {self.email}\nEndereço: {self.address.street}\nNúmero: {self.address.number}\nBairro: {self.address.neighborhood}\nCidade: {self.address.city}\nEstado: {self.address.state}")