def divisoresProprios(x):
    divisores = []
    i = 1
    while i < x:
        if x % i == 0:
            divisores.append(i)
        i += 1
    return divisores

n = int(input())
for i in range(n):
    x = int(input())
    if x == sum(divisoresProprios(x)):
        print("%d eh perfeito" % x)
    else:
        print("%d nao eh perfeito" % x)
