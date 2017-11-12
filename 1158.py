n = int(input())
for i in range(n):
    x,y = [int(z) for z in input().split()]
    soma = 0
    i = 0
    while i < y:
        if x % 2 != 0:
            soma += x
            i += 1
        x += 1
    print(soma)
