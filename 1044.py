v = [int(x) for x in input().split()]
v = sorted(v)
if v[1] % v[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
