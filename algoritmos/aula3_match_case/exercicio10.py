# Sistema de Pagamento

"""
O usuário escolhe uma forma de pagamento e o programa informa se há desconto ou acréscimo.
"""

print("=====ITAÚ=====")
print("Bem vindo ao Itaú! \nEscolha a forma de pagamento")

print("\n=====FORMAS DE PAGAMENTO=====")
print("1 - Dinheiro em espécie \n2 - Cheque \n3 - Cartão de crédito \n4 - Cartão de débito \n5 - Boleto bancário \n6 - Depósito e transferência bancária")
forma_pgto = input("Escolha a forma de pagamento: ")

match forma_pgto:
    case "1" | "Dinheiro em espécie" | "dinheiro em espécie" | "Dinheiro em especie" | "dinheiro em especie":
        print("\n=====DINHEIRO EM ESPÉCIE=====")
        print("Será aplicado um desconto de 10%")
    case "2" | "Cheques" | "cheques":
        print("\n=====CHEQUE=====")
        print("Será aplicado um acréscimo de 5%")
    case "3" | "Cartão de crédito" | "cartão de crédito" | "cartão de crédito" | "cartão de credito":
        print("\n=====CARTÃO DE CRÉDITO=====")
        print("Será aplicado um acréscimo de 5%")
    case "4" | "Cartão de débito" | "cartão de débito":
        print("\n=====CARTÃO DE DÉBITO=====")
        print("Será aplicado um desconto de 3%")
    case "5" | "Boleto bancário" | "boleto bancário":
        print("\n=====BOLETO BANCÁRIO=====")
        print("Será aplicado um desconto de 5%")
    case "6" | "Depósito e transferência bancária" | "Depósito" | "Transferência":
        print("\n=====DEPÓSITO E TRANSFERÊNCIA BANCÁRIA=====")
        print("Será aplicado um desconto de 7%")
    case _:
        print("\nOpção inválida!")