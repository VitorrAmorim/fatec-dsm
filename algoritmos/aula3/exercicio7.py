# Calculadora Simples

"""
O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado.
"""

print("=====CALCULADORA ONLINE=====\n")
operacao = input("Escolha uma das operações abaixo \nSoma (+) \nSubtração (-) \nMultiplicação (*) \nDivisão (/) \nDigite a opção: ")
num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))

match operacao:
    case "Soma" | "soma" | "+":
        print("=====RESULTADO=====")
        print(f"\nO resultado da soma é de {num1 + num2:.2f}")
    case "Subtração" | "subtração" | "-":
        print("=====RESULTADO=====")
        print(f"\nO resultado da subtração é de {num1 - num2:.2f}")
    case "Multiplicação" | "multiplicação" | "*":
        print("=====RESULTADO=====")
        print(f"\nO resultado da multiplicação é de {num1 * num2:.2f}")
    case "Divisão" | "divisã0" | "/":
        print("\n=====RESULTADO=====")
        print(f"O resultado da divisão é de {num1 / num2:.2f}")
    case _:
        print("\nDados inválidos!")