def adjacentes(no, m, n):
    adj = []
    i,j = no[0], no[1]
    if i == 0 and j == 0:
        adj.extend([(0,1),(1,0)])
    elif i == m and j == n:
        adj.extend([(m-1,n),(m,n-1)])
    elif i == 0 and j == n:
        adj.extend([(0,n-1),(1,n)])
    elif i == m and j == 0:
        adj.extend([(m,n-1),(m-1,n)])
    elif i == 0:
        adj.extend([(0,j+1),(0,j-1),(1,j)])
    elif i == m:
        adj.extend([(m,j+1),(m,j-1),(m-1,j)])
    elif j == 0:
        adj.extend([(i+1,0),(i-1,0),(i,1)])
    elif j == n:
        adj.extend([(i+1,n),(i-1,n),(i,n-1)])
    else:
        adj.extend([(i+1,j),(i-1,j),(i,j+1),(i,j-1)])
    return adj

def bfs(grafo, s, m, n):
    keys = grafo.keys()
    visitados = []
    fila = []
    fila.append(s)
    while fila:
        no = fila.pop(0)
        visitados.append(no)
        if no in keys and grafo[no] == 0:
            return no
        adj = adjacentes(no, m, n)
        for a in adj:
            if a not in visitados and a not in fila:
                fila.append(a)

def maisProximo(chamada, sedes):
    #distancia = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
    mp = chamada
    md = 999999999999999
    for s in sedes:
        #d = distancia(chamada, s)
        d = abs(chamada[0] - s[0]) + abs(chamada[1] - s[1])
        if d < md:
            mp = s
            md = d
        elif d == md:
            if s[0] < mp[0]:
                mp = s
                md = d
            elif s[0] == mp[0]:
                if s[1] < mp[1]:
                    mp = s
                    md = d
    return mp

inst = 1
while True:
    m,n = [int(x) for x in input().split()]
    if m == 0 or n == 0:
        break
    print("Instancia %d" % inst)
    inst += 1
    g = {}
    nSedes = int(input())
    sedes = []
    for i in range(nSedes):
        x,y = [int(z) for z in input().split()]
        g[x,y] = 0
        sedes.append((x,y))
    nChamadas = int(input())
    for i in range(nChamadas):
        x,y = [int(z) for z in input().split()]
        g[x,y] = 1
        #si,sj = bfs(g,c,m,n)
        si, sj = maisProximo((x,y),sedes)
        print("%d %d" % (si,sj))
    
