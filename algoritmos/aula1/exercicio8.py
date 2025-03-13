# Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados

largura = float(input("Digite a largura da parede:"))
altura = float(input("Digite a altura da parede:"))
area = largura * altura
tinta = area / 2
print(f"A área é de {area:.2f} e a quantidade de tinta é de {tinta}")