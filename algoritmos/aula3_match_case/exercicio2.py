# Cálculo de Área de Figuras Geométricas

# Desenvolva um programa que permita ao usuário escolher entre calcular a área de um quadrado, retângulo ou triângulo e insira os valores necessários para o cálculo.

print("=====CALCULADOR DE ÁREA DE FIGURAS GEOMÉTRICAS=====")

opcao = input("Escolha a opção (quadrado, retângulo ou triângulo) para o cálculo: ")
base = float(input("Digite a medida da base: "))
altura = float(input("Digite a medida da altura: "))

match opcao:
    case "Quadrado" | "quadrado":
        print(f"A área do quadrado é de {base*altura:.2f}")
    case "Retângulo" | "Retangulo":
        print(f"A área do retângulo é de {base * altura:.2f}")
    case "Triângulo":
        print(f"A área do triângulo é de {base * altura / 2:.2f}")
    case _:
        print("Dados inválidos!")