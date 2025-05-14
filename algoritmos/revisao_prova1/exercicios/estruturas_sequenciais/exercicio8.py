"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""

ganho = float(input("Dite quantos Reais (R$) você ganha por hora: "))
horas = int(input("Quantas horas você trabalhou no mês?: "))
salario = ganho * horas

print(f"Seu salário nesse mês foi de {salario}")