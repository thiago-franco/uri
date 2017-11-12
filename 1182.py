n = int(input())
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
for x in m:
    soma += x[n]
if a == "S":
    print("%.1f" % soma)
elif a == "M":
    media = soma/12
    print("%.1f" % media)
        
