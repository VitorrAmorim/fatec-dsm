# Tradutor de Cores

"""
O usuário informa uma cor em português (vermelho, azul, verde, amarelo),
e o programa exibe sua tradução para inglês.
"""

print("=====GOOGLE TRADUTOR=====")
print("Bem vindo ao Google Tradutor!\n \nEscolha entre uma das cores abaixo para ser traduzida para inglês")
print("Vermelho \nAzul \nVerde \nAmarelo")
cor = input("Digite a cor desejada: ")

match cor:
    case "Vermelho" | "vermelho":
        print("\n=====TRADUZINDO...=====")
        print(f"COR EM PORTUGUÊS: {cor} \nCOR EM INGLÊS: Red")
    case "Azul" | "azul":
        print("\n=====TRADUZINDO...=====")
        print(f"COR EM PORTUGUÊS: {cor} \nCOR EM INGLÊS: Blue")
    case "Verde" | "verde":
        print("\n=====TRADUZINDO...=====")
        print(f"COR EM PORTUGUÊS: {cor} \nCOR EM INGLÊS: Green")
    case "Amarelo" | "amarelo":
        print("\n=====TRADUZINDO...=====")
        print(f"COR EM PORTUGUÊS: {cor} \nCOR EM INGLÊS: Yellow")
    case _:
        print("\nA tradução para esta cor não está disponível no momento! Por favor, tente novamente mais tarde.")