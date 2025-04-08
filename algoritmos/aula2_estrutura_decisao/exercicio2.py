# Solicite a idade do usuário e informe se ele é menor de idade, maior de idade ou idoso (considerando 18 e 65 anos como limites).

idade = int(input("Digite a idade:"))

if idade <= 17:
    print("Menor de idade")
elif idade <= 65:
    print("Adulto")
else:
    print("Idoso")