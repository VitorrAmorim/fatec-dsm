# Cálculo de Desconto por Categoria

""""
O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis),
e o programa exibirá o percentual de desconto correspondente.
"""

print("=====AMERICANAS====")
print("Bem vindo ao site da Americanas")
print("Escolha entre o tipo de produto abaixo para eventual aplicação de desconto \n1 - Eletrônico \n2 - Roupas \n3 - Alimentos \n4 - Móveis")
produto = input("Digite o tipo de produto: ")

match produto:
    case "1" | "Eletrônico" | "Eletronico" | "eletrônico" | "eletronico":
        print("=====ELETRÔNICOS=====")
        print("Desconto de 10% aplicado para qualquer dispositivo eletrônico!")
    case "2" | "Roupas" | "roupas":
        print("=====ROUPAS=====")
        print("Desconto de 15% aplicado para qualquer roupa!")
    case "3" | "Alimentos" | "alimentos":
        print("=====ALIMENTOS=====")
        print("Desconto de 12% aplicado para qualquer alimento!")
    case "4" | "Móveis" | "Moveis" | "móveis" | "moveis":
        print("=====MÓVEIS=====")
        print("Desconto de 8% aplicado para qualquer móvel!")
    case _:
        print("Opção não encontrada! Digite uma opção válida.")