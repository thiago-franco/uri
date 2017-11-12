I = []
G = []

while True:
    i,g = [int(x) for x in input().split()]
    I.append(i)
    G.append(g)
    print("Novo grenal (1-sim 2-nao)")
    c = int(input())
    if c == 2:
        break

print("%d grenais" % len(I))
vi = 0
vg = 0
e = 0
for n in range(len(I)):
    if I[n] > G[n]:
        vi += 1
    elif G[n] > I[n]:
        vg += 1
    else:
        e += 1
print("Inter:%d" % vi)
print("Gremio:%d" % vg)
print("Empates:%d" % e)
if vi > vg:
    print("Inter venceu mais")
elif vg > vi:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")


