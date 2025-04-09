# Tabuada de um Número

"""
Peça ao usuário um número e exiba a tabuada desse número de 1 a 10
"""

num = int(input("Digite um número para a tabuada: "))

for tabuada in range(1, 11):
    print(f" {num} x {tabuada} é igual a {num * tabuada}")