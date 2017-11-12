n = int(input())
x = []
for i in range(n):
    x.append(int(input()))
    
dentro = [s for s in x if s in range(10, 21)]
print("%d in" % len(dentro))
print("%d out" % int(len(x) - len(dentro)))
