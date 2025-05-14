"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

salario = float(input("Digite o quanto em R$ você ganha por hora: "))
horas = int(input("Digite o total de horas trabalhadas no mês: "))
salarioBruto = salario * horas
impostoRenda = salarioBruto * (11 / 100)
inss = salarioBruto * (8 / 100)
sindicato = salarioBruto * (5 / 100)
salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print(f"+ Salário Bruto : R${salarioBruto:.2f}\n"
      f"- IR (11%) : R${impostoRenda:.2f}\n"
      f"- Sindicato ( 5%) : R${sindicato:.2f}\n"
      f"= Salário Liquido : R${salarioLiquido:.2f}")