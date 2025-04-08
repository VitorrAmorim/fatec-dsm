# Simulação de Atendimento Telefônico

"""
O usuário seleciona uma opção de atendimento telefônico:

1 - Suporte Técnico
2 - Financeiro
3 - Cancelamento
4 - Falar com um atendente
"""

print("=====ITAÚ=====")
print("\nBem vindo a central de atendimento telefônico do banco Itaú! Como podemos te ajudar?")
print("1 - Suporte Técnico \n2 - Financeiro \n3 - Cancelamento \n4 - Falar com um atendente")
opcao = input()

match opcao:
    case "1" | "Suporte Técnico" | "Suporte Tecnico" | "suporte técnico" | "suporte tecnico" | "suporte":
        print("\n=====SUPORTE TÉCNICO=====")
        print("Você esta sendo redirecionado para o canal de atendimento técnico, aguarde...")
    case "2" | "Financeiro" | "financeiro":
        print("\n=====FINANCEIRO=====")
        print("Você esta sendo redirecionado para o canal de atendimento financeiro, aguarde...")
    case "3" | "Cancelamento" | "cancelamento" | "cancelar":
        print("\n=====CANCELAMENTO=====")
        print("Você esta sendo redirecionado para o canal de cancelamento, aguarde...")
    case "4" | "Falar com um atendente" | "falar com um atendente" | "atendente":
        print("\n=====FALAR COM UM ATENDENTE=====")
        print("Você esta sendo redirecionado para um atendente, aguarde...")
    case _:
        print("\nOpção não disponível! Selecione uma opção válida.")