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
if a == "S":
    print("%.1f" % sum(m[n]))
elif a == "M":
    media = float(sum(m[n]))/12
    print("%.1f" % media)
        
