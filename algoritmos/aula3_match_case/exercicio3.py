# Sistema de Login Simples

"""
O programa deve pedir ao usuário que informe seu nome de usuário e, com base nisso, conceder um nível de acesso:
Admin → Acesso total
Professor → Acesso ao ambiente acadêmico
Aluno → Acesso ao ambiente de estudos
"""

print("=====LOGIN=====")
nome = input("Para que possa acessar a plataforma, digite seu nome: ")

match nome:
    case "Vitor" | "vitor":
        print("Bem vindo a página de acesso total de administrador!")
    case "Lucas" | "lucas":
        print("Bem vindo ao ambiente acadêmico!")
    case _:
        print("Bem vino ao ambiente de estudos!")
