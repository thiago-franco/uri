a = str(input())
m = {}
for i in range(12):
    for j in range(12):
        x = float(input())
        m[i,j] = x
soma = 0
tam = 0
j = 0
k = 1
while j < 12:
    if k == 12-k-1:
        break
    i = k
    while i <= 12-k-1:
        soma += m[i,j]
        i += 1
        tam += 1
    k += 1
    j += 1
    
if a == "S":
    print("%.1f" % soma)
elif a == "M":
    media = soma/tam
    print("%.1f" % media)


