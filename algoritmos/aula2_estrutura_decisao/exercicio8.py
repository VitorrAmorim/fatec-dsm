# Peça ao usuário seu peso e altura, calcule o Índice de Massa Corporal (IMC) e classifique-o como "Abaixo do peso", "Peso normal", "Sobrepeso" ou "Obesidade".

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura**2)

if imc <= 18.4:
    print(f"Abaixo do peso! Seu IMC é de {imc:.2f}")
elif imc <= 24.9:
    print(f"Peso normal! Seu IMC é de {imc:.2f}")
elif imc <= 29.9:
    print(f"Sobrepeso! Seu IMC é de {imc:.2f}")
else:
    print(f"Obesidade! Seu IMC é de {imc:.2f}")