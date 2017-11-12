

casos = int(input())
i = 0
while i < casos:
    nome, lv = [x for x in input().split()]
    stats = []
    for j in range(0,4):
        bs, iv, ev = [int(x) for x in input().split()]
        s = 0
        if j == 0:
            s = ((iv + bs + (ev**0.5)/8 + 50) * int(lv))/ 50 + 10
        else:
            s = ((iv + bs + (ev**0.5)/8) * int(lv))/ 50 + 5
        stats.append(s)
    i += 1
    print("Caso #%d: %s nivel %d" % (i, nome, int(lv)))
    print("HP: %d" % (stats[0]))
    print("AT: %d" % (stats[1]))
    print("DF: %d" % (stats[2]))
    print("SP: %d" % (stats[3]))
