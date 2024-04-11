def main():
    from address import Address
    from client import Client

    endereco_cliente = Address("Rua Carlos Speicher", 68, "Vila Nova", "Rio Negrinho", "SC")
    cliente = Client("Eduardo José Schroeder", "09803383957", 47991858165, "eduardoj.schroeder@gmail.com", endereco_cliente)
    cliente.PrintClient()

if __name__ == "__main__":
    main()