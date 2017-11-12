n = int(input())
v = [int(x) for x in input().split()]
menor = 999999999999
indice = -1
for i, x in enumerate(v):
    if x < menor:
        menor = x
        indice = i
print("Menor valor: %d" % menor)
print("Posicao: %d" % indice)
