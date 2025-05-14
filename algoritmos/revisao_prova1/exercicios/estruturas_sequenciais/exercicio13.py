"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7
"""

altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))
homem = (72.7 * altura) - 58
mulher = (62.1 * altura) - 44.7

print(f"O peso ideal para homens é de {homem:.2f}")
print(f"O peso ideal para mulheres é de {mulher:.2f}")