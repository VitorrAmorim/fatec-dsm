# Exercício 4 - Sistema de Controle de Quarto – Limite de Pessoas

"""
Um quarto de hotel suporta até 3 pessoas. Crie um sistema com while que permita
registrar pessoas até atingir o limite.
A cada pessoa, exiba: "Pessoa registrada".
Quando atingir 3, exiba: "Limite atingido".
"""

contador = 0

while contador < 3:
    input(f"Digite o nome da pessoa: ")
    contador += 1
    print("Pessoa registrada")

print("Limite atingido!")