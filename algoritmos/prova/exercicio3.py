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