# A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90,00 por dia e R$0,20 por Km rodado.

km = float(input("Digite a quantidade de Km percorridos:"))
dias = int(input("Digite a quantidade de dias alugados:"))
custoDiaria = dias * 90.00
custoKm = km * 0.20
total = custoKm * custoDiaria
print(f"O custo total é de R${total:.2f}")
