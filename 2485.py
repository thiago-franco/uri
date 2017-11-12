n = int(input())
for i in range(n):
    a,b = [int(c) for c in input().split()]
    grafo = {}
    for i in range(1,a+1):
        linha = [l for l in input().split()]
        for j, l in enumerate(linha):
            if l == '1':
                grafo[i,j+1] = l

    dias = -1
    x,y = [int(z) for z in input().split()]
    goiabeiras = [(x,y)]
    while grafo:
        adjacentes = []
        for g in goiabeiras:
            valido = lambda w: w in grafo and w not in goiabeiras and w not in adjacentes
            if valido((g[0],g[1]+1)):
                adjacentes.append((g[0],g[1]+1))
            if valido((g[0]+1,g[1])):
                adjacentes.append((g[0]+1,g[1]))
            if valido((g[0],g[1]-1)):
                adjacentes.append((g[0],g[1]-1))
            if valido((g[0]-1,g[1])):
                adjacentes.append((g[0]-1,g[1]))
            if valido((g[0]+1,g[1]+1)):
                adjacentes.append((g[0]+1,g[1]+1))
            if valido((g[0]-1,g[1]+1)):
                adjacentes.append((g[0]-1,g[1]+1))
            if valido((g[0]+1,g[1]-1)):
                adjacentes.append((g[0]+1,g[1]-1))
            if valido((g[0]-1,g[1]-1)):
                adjacentes.append((g[0]-1,g[1]-1))
            grafo.pop(g)
        dias += 1
        goiabeiras = adjacentes

    print(dias)
    

