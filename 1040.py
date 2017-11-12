notas = [float(a) for a in input().split()]
n1 = notas[0]
n2 = notas[1]
n3 = notas[2]
n4 = notas[3]
media = (2*n1 + 3*n2 + 4*n3 + n4)/10
print("Media: %.1f" % media)
if media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media <= 6.9:
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame: %.1f" % ne)
    me = (media+ne)/2
    if me >= 5:
        print("Aluno aprovado.")
        print("Media final: %.1f" % me)
    else:
        print("Aluno reprovado.")
else:
    print("Aluno aprovado.")
