"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.
"""

numInt1 = int(input("Dite o 1° número inteiro: "))
numInt2 = int(input("Dite o 2° número inteiro: "))
numReal = float(input("Dite o número real: "))
dobro = (numInt1 * 2) + (numInt2 / 2)
triplo = (numInt1 * 3) + numReal
cubo = numReal ** 3

print(f"O produto do dobro de {numInt1} mais a a metade de {numInt2} é de {dobro:.2f}")
print(f"A soma do triplo de {numInt1} mais {numReal} é de {triplo:.2f}")
print(f"{numReal} elevado ao cubo é {cubo:.2f}")