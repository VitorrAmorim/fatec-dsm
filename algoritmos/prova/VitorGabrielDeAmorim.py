# Exercício 1 - Sistema de Hotel - Verificação de Diárias

"""
Um sistema de hotel deve calcular o valor total da hospedagem. O usuário informa o
número de diárias. Cada diária custa R$ 120.
Se o número de diárias for maior que 7, o sistema aplica um desconto de 10% no total.
Desenvolva esse algoritmo com uso de operadores e estrutura de decisão
"""

diaria = int(input("Digite o número de diárias desejadas: "))
valor = 120
total = diaria * valor

if diaria > 7:
    desconto = total * 0.10
    total -= desconto

print(f"O valor total da(s) diária(s) é de R${total:.2f}")



# Exercício 2 - Sistema de Restaurante - Pedido Adcional

"""
Um sistema de restaurante oferece dois pratos:
• Prato A: R$ 20
• Prato B: R$ 25
O cliente pode ainda adicionar uma bebida por R$ 5.
Desenvolva um algoritmo que pergunte qual prato foi escolhido (A ou B), se
deseja bebida (S ou N) e calcule o valor total do pedido.
"""

prato = input("Digite qua o prato desejado (A ou B): ")
bebida = input("Deseja bebida (S ou N)?: ")

if prato == "A":
    valorPrato = 20.00
    print(f"O valor do prato {prato} é de R${valorPrato}")
elif prato == "B":
    valorPrato = 25.00
    print(f"O valor do prato {prato} é de R${valorPrato}")
else:
    print("Resposta inválida!")

if bebida == "S":
    valorBebida = 5.00
    print(f"O valor da bebida e do prato ({prato}) juntos é de R${valorBebida + valorPrato}")
elif bebida == "N":
    print("Obrigado pela preferência!")
else:
    print("Resposta inválida!")



# Exercício 3 - Pedido de Comida – Soma de Pedidos

"""
Um sistema de lanchonete recebe o valor de vários pedidos feitos no caixa.
Os pedidos são feitos em sequência até que o valor 0 seja digitado.
Calcule e exiba o total da conta usando while.
"""

total = 0

while True:
    valor = float(input("Digite o valor do pedido: "))
    if valor == 0:
        break

    total += valor

print(f"O valor total dos pedidos é de R${total:.2f}")



# Exercício 4 - Sistema de Controle de Quarto – Limite de Pessoas

"""
Um quarto de hotel suporta até 3 pessoas. Crie um sistema com while que permita
registrar pessoas até atingir o limite.
A cada pessoa, exiba: "Pessoa registrada".
Quando atingir 3, exiba: "Limite atingido".
"""

contador = 0

while contador < 3:
    input(f"Digite o nome da pessoa: ")
    contador += 1
    print("Pessoa registrada")

print("Limite atingido!")