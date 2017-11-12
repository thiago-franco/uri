v = []
i = 0
while i < 20:
    vi = int(input())
    v.append(vi)
    i += 1

for i in range(0,int(len(v)/2)):
    aux = v[i]
    v[i] = v[len(v)-i-1]
    v[len(v)-i-1] = aux

i = 0
while i < len(v):
    print("N[%d] = %d" % (i, v[i]))
    i += 1
