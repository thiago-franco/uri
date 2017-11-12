def somaNPares(x, n):
    soma = 0
    i = 0
    while i < n:
        if x % 2 == 0:
            soma += x
            i += 1
        x += 1
    return soma

while True:
    x = int(input())
    if x == 0:
        break
    print(somaNPares(x, 5))
