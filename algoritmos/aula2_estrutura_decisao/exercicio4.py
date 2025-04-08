# Crie uma calculadora simples que permita ao usuário escolher uma operação (adição, subtração, multiplicação ou divisão) e dois números, e então exiba o resultado.

escolha = input("Escolha a operação (adição, subtração, divisão, multiplição):")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
adicao = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

if escolha == "Adição":
    print(adicao)
elif escolha == "Subtração":
    print(subtracao)
elif escolha == "Divisão":
    print(divisao)
elif escolha == "Multiplicação":
    print(multiplicacao)