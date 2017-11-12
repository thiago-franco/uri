def adjacente(estado, direcaoAtual):
    if direcaoAtual == '>' and (estado[0], estado[1]+1) in grafo.keys():
        return (estado[0], estado[1]+1)
    elif direcaoAtual == '<' and (estado[0], estado[1]-1) in grafo.keys():
        return (estado[0], estado[1]-1)
    elif direcaoAtual == '^' and (estado[0]-1, estado[1]) in grafo.keys():
        return (estado[0]-1, estado[1])
    elif direcaoAtual == 'v' and (estado[0]+1, estado[1]) in grafo.keys():
        return (estado[0]+1, estado[1])

def dfs(inicio, fim, grafo, direcoes, direcaoAtual):
    visitados = []
    pilha = []
    pilha.append(inicio)
    while pilha:
        no = pilha.pop()
        visitados.append(no)
        if grafo[no] == fim:
            return True
        elif grafo[no] in direcoes:
            direcaoAtual = grafo[no]
        adj = adjacente(no, direcaoAtual)
        if adj and adj not in visitados:
            pilha.append(adj)

def dfsRecursivo(no, fim, grafo, direcoes, direcaoAtual):
    if grafo[no] == fim:
        return True
    elif grafo[no] in direcoes:
        direcaoAtual = grafo[no]
    adj = adjacente(no, direcaoAtual)
    if adj:
        grafo.pop(no)
        return dfsRecursivo(adj, fim, grafo, direcoes, direcaoAtual)

y = int(input())
x = int(input())
grafo = {}
direcaoAtual = ''
direcoes = ['>', '<', '^', 'v']
fim = '*'
for i in range(x):
    linha = [l for l in list(input())]
    for j in range(y):
        grafo[i,j] = linha[j]
if dfs((0,0), fim, grafo, direcoes, direcaoAtual):
    print("*")
else:
    print("!")
