km = float(input("Digite a quantidade de Km percorridos:"))
dias = int(input("Digite a quantidade de dias alugados:"))
custoDiaria = dias * 90.00
custoKm = km * 0.20
total = custoKm * custoDiaria
print(f"O custo total é de R${total:.2f}")