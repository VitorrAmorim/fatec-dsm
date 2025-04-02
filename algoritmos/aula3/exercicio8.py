# Sistema de Reserva de Passagens

"""
O usuário escolhe um destino (São Paulo, Rio de Janeiro, Curitiba, Salvador) e recebe o valor da passagem.
"""

print("=====LATAM=====")
print("Bem vindo ao site da Latam! \nEscolha o destino abaixo para consultar o valor da passagem")
print("\nSão Paulo - SP \nRio de Janeiro - RJ \nCuritiba - PR \nSalvador - BH")
destino = input("Digite o destino desejado: ")

match destino:
    case "São Paulo" | "são paulo" | "Sao Paulo" | "são paulo" | "sp" | "SP":
        print("\n=====SÃO PAULO - SP=====")
        print("A passagem com destino a São Paulo - SP é de R$232,00")
    case "Rio de Janeiro" | "rio de janeiro" | "rio" | "RJ" | "rj":
        print("\n=====RIO DE JANEIRO - RJ=====")
        print("A passagem com destino a Rio de Janeiro - RJ é de R$394,00")
    case "Curitiba" | "curitiba" | "PR" | "pr":
        print("\n=====CURITIBA - PR=====")
        print("A passagem com destino a Curitiba - PR é de R$362,00")
    case "Salvador" | "salvador" | "BH" | "bh":
        print("\n=====SALVADOR - BH=====")
        print("A passagem com destino a Salvador - BH é de R$482,00")
    case _:
        print("\nDestino não encontrado!")