# Soma dos Números de 1 a N

"""
Solicite um número ao usuário e exiba a soma de 1 até esse número
"""

num = int(input("Digite um número: "))

for numero in range(0, num, +1):
    print(numero +1)