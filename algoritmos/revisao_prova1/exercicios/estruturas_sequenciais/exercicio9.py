"""
Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
"""

farenheit = int(input("Dite a temperatura em graus Farenheit: "))
celsius = (5 * (farenheit - 32) / 9)

print(f"{farenheit} graus Farenheit são {celsius:.2f} graus Celsius")