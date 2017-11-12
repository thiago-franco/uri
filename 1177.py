t = int(input())
c = 0
for i in range(1000):
    if c == t:
        c = 0
    print("N[%d] = %d" % (i, c))
    c += 1
