''' String '''
print('Olá Mundo!') #String é o conjunto de caracteres

mensagem = "Olá"
print(mensagem)

mensagem = mensagem + " Mundo" + "!" #O sinal de soma pode ser aplicado como um concatenador de Strings
print(mensagem)


''' Números Inteiros '''
print(1 + 1) #Soma

print(5 - 8) #Subtração

print(4567 * 9) #Multiplicação

print(300 / 78900) #Divisão

print(2 ** 2) #Potênciação

print(2 + 3 * 4) #A multiplicação tem precedência sobre a soma

print((2 + 3) * 4) #A soma tem precedência sobre a multiplicação


''' Ponto Flutuante '''
'''Python chama qualquer número com um ponto decimal de número de ponto flutuante (float). Esse termo é utilizado na maioria das linguagens de programação e refere-se ao fado de um ponto decimal poder aparecer em qualquer posição de um número.'''
print(0.1 + 0.1) #Soma

print(0.567 - 0.111) #Subtração

#Dica
result = 0.567 - 0.111
print("%.3f" % result)

print(2 * 0.268) #Multiplicação

#ATENÇÃO
'''
idade = 19
print("Feliz aniversário de " + idade + " anos!") #Isso não funciona, pois idade é um número inteiro e não uma string
'''
#A função str() encapsula um valor númerico e te ajuda na hora de concatenar
idade = 19
print("Feliz aniversário de " + str(idade) + " anos!") #Isso funciona, pois idade é uma string


''' Operadores Aritméticos '''
print(1 + 879) #Soma

print(456 - 79) #Subtração

print(789 * 456) #Multiplicação

print(789456 / 3) #Divisão Inteira

print(789456 % 5) #Resto da Divisão

print(3 ** 3) #Potênciação