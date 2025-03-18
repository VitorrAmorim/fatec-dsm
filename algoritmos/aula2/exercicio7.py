# Receba a nota de um aluno e classifique-a como A (90-100), B (80-89), C (70-79), D (60-69), ou F (menos de 60).

nota = int(input("Digite a nota: "))

if nota <= 59:
    print("F")
elif nota <= 69:
    print("D")
elif nota <= 79:
    print("C")
elif nota <= 89:
    print("B")
else:
    print("A")