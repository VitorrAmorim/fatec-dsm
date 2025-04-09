# Média de Notas

"""
Peça 5 notas ao usuário e calcule a média delas
"""

soma = 0

for i in range(5):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    soma += nota

media = soma / 5
print(f"A média das notas é: {media:.2f}")