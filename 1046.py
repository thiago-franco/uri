i, f = [int(x) for x in input().split()]

if i >= f:
    d = 24 - i + f
else:
    d = f - i
print("O JOGO DUROU %d HORA(S)" % d)
