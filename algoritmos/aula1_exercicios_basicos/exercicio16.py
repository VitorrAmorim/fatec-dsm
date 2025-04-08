# Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25,00 por hora trabalhada

dias = int(input("Digite os dias trabalhados:"))
horas = dias * 8
salario = horas * 25.00
print(f"Horas trabalhadas: {horas}, Salario: {salario}")