# Desenvolva um programa que permita ao usuário escolher uma operação (saque, depósito) e simule o comportamento de um caixa eletrônico com validações básicas (ex.: saldo insuficiente para saque).
deposito = float(input("Digite um valor para depósito: "))
saque = float(input("Escolha um valor para saque: "))

if saque <= deposito:
    print(f"Operação realizada com sucesso! Seu atual saldo bancário é de {deposito - saque:.2f}")
else:
    print(f"Saldo insuficiente!")