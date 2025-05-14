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