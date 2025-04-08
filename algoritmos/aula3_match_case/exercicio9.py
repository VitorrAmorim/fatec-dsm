# Simulador de Compra em Loja Online

"""
O usuário escolhe um produto e o programa informa o preço.
"""

print("=====SAMSUMNG=====")
print("Bem vindo ao ao site oficial Samsung!\n \nEscolha um dispositivo abaixo para consultar seu preço")
print("Samsung Galaxy S25 Ultra \nSamsung Galaxy S25 \nSamsung Galaxy S24 Ultra \nSamsung Galaxy S24 \nSamsung Galaxy S23 Ultra \nSamsung Galaxy S23")
dispositivo = input("\nDigite o dispositivo: ")

match dispositivo:
    case "Samsung Galaxy S25 Ultra" | "Galaxy S25 Ultra" | "S25 Ultra":
        print("\n=====SAMSUNG GALAXY S25 ULTRA=====")
        print("O preço do dispositivo é de R$ 7.140")
    case "Samsung Galaxy S25" | "Galaxy S25" | "S25":
        print("\n=====SAMSUNG GALAXY S25=====")
        print("O preço do dispositivo é de R$ 4.979")
    case "Samsung Galaxy S24 Ultra" | "Galaxy S24 Ultra" | "S24 Ultra":
        print("\n=====SAMSUNG GALAXY S24 ULTRA=====")
        print("O preço do dispositivo é de R$ 5.219")
    case "Samsung Galaxy S24" | "Galaxy S24" | "S24":
        print("\n=====SAMSUNG GALAXY S24=====")
        print("O preço do dispositivo é de R$ 3.149")
    case "Samsung Galaxy S23 Ultra" | "Galaxy S23 Ultra" | "S23 Ultra":
        print("\n=====SAMSUNG GALAXY S23 ULTRA=====")
        print("O preço do dispositivo é de R$ 4.707,60")
    case "Samsung Galaxy S23" | "Galaxy S23" | "S23":
        print("\n=====SAMSUNG GALAXY S23=====")
        print("O preço do dispositivo é de R$ 3.399")
    case _:
        print("\nProduto não encontrado!")