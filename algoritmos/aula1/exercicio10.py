# Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos"

a = float(input("Digite o 1° valor:"))
b = float(input("Digite o 2° valor:"))

if a % b == 0:
    print("Sao múltiplos")
else:
    print("Não é múltiplos")