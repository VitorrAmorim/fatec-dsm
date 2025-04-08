# Solicite o preço de um produto e aplique um desconto de 10% se o preço for maior que R$ 100. Exiba o valor final.

preco = float(input("Digite o preço do produto: "))

if preco <= 100.00:
    print(f"Sem desconto! O valor do produto é de {preco:.2f}")
else:
    desconto = preco - (preco * 0.10)
    print(f"Desconto aplicado! O valor do produto é de {desconto:.2f}")