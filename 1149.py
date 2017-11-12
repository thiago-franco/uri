i = [int(x) for x in input().split()]
a = i.pop(0)
n = 0
for x in i:
    if x > 0:
        n = x
        break
s = sum([x for x in range(a, a+n)])
print(s)
    
