# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor

custo = float(input("Digite o preço original:"))
distribuidor = custo + (custo * 0.28)
imposto = distribuidor + (distribuidor * 0.45)
print(distribuidor, imposto)
print(f"O preço será de {imposto}")