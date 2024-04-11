class Address:
    def __init__(self, street, number, neighborhood, city, state):
        self.street = street
        self.number = number
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def ChangeAddress(self, street, number, neighborhood, city, state):
        self.street = street if self.street != street else self.street
        self.number = number if self.number != number else self.number
        self.neighborhood = neighborhood if self.neighborhood != neighborhood else self.neighborhood
        self.city = city if self.city != city else self.city
        self.state = state if self. state != state else self.state