"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
"""

celsius = int(input("Digite a temperatura em Celsius: "))
farenheit = (5 / (celsius + 32) * 9)

print(f"{celsius} graus Celsius são {farenheit:.2f} graus Farenheit")