a = str(input())
m = [[]]
j = 0
k = 0
for i in range(144):
    if j == 12:
        j = 0
        m.append([])
        k += 1
    x = float(input())
    m[k].append(x)
    j += 1
soma = 0
tam = 0
for idx, x in enumerate(m):
    x = x[:idx]
    tam += len(x)
    soma += sum(x)
if a == "S":
    print("%.1f" % soma)
elif a == "M":
    media = soma/tam
    print("%.1f" % media)
