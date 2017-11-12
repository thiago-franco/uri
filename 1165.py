def ehPrimo(x):
    divisores = 0
    i = 2
    while i <= int(x/2):
        if x % i == 0:
            divisores += 1
        if divisores > 0:
            return False
        i += 1
    return True

n = int(input())
for i in range(n):
    x = int(input())
    if ehPrimo(x):
        print("%d eh primo" % x)
    else:
        print("%d nao eh primo" % x)
