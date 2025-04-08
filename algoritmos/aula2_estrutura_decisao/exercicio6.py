# Crie um programa que simule um sistema de login. Solicite um nome de usuário e senha e verifique se as credenciais estão corretas.

nomeUsuario = input("Digite o nome de usúario: ")
idade = int(input("Digite sua idade: "))
confirmarUsuario = input("Digite o usúario novamente: ")
confirmarIdade = int(input("Digite a idade novamente: "))

if nomeUsuario == confirmarUsuario and idade == confirmarIdade:
    print("Dados válidos")
else:
    print("Dados inválidos")