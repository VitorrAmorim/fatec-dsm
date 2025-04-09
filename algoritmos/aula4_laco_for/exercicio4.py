# Contagem com Passo Personalizado

"""
Peça ao usuário três números: início, fim e passo e exiba a sequência correspondente
"""

numInicio = int(input("Digite o número inicial: "))
numFim = int(input("Digite o número final: "))
numPasso = int(input("Digite um número para incremento: "))

for numero in range(numInicio, numFim, numPasso):
    print(numero)