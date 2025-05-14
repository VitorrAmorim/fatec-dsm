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