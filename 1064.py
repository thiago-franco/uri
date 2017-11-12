a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
l = [a,b,c,d,e,f]
p = list()
for i in l:
    if i > 0:
        p.append(i)
m = 0
for i in p:
    m += i
m = m/len(p)

print("%d valores positivos" % len(p))
print("%.1f" % m)
