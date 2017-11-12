def impar(x):
    return x % 2 != 0

x = int(input())
i = 0
if impar(x):
    print(x)
    i += 1
while i < 6:
    x += 1
    if impar(x):
        print(x)
        i += 1

    
