n = int(input())
paresQuadrados = [int(x) for x in range(1, n+1) if x%2 == 0]
for p in paresQuadrados:
    print("%d^2 = %d" % (p,p**2))
