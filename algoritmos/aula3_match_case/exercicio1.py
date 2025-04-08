# Conversor de Moedas

# Implemente um conversor de moedas que permita ao usuário escolher entre Dólar (USD), Euro (EUR) e Libra (GBP) e converter um valor informado para Reais (BRL).

print("=====CONVERSOR DE MOEDAS=====")
opcao = input("Digite a moeda desejada (dólar, euro ou libra): ")
valor = float(input("Digite o valor: "))

match opcao:
    case "dólar" | "Dólar" | "USD" | "usd":
        print(f"O valor convertido para real é de {valor*5.70:.2f}")
    case "euro" | "Euro" | "EUR" | "eur":
        print(f"O valor convertido para real é de {valor*6.15:.2f}")
    case "libra" | "Libra" | "GBP" | "gbp":
        print(f"O valor convertido para real é de {valor*7.35:.2f}")
    case _:
        print("Dados inválidos!")