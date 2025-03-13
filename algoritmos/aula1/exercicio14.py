# Peça a quantidade de kWh consumidos e o valor por kWh, depois calcule o valor da conta de energia

quantidade = float(input("Digite a quantidade de kWh:"))
valor = float(input("Digite o valor por kWh:"))
valorConta = quantidade / valor
print(f"O valor é de R${valorConta:.2f}")