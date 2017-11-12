x = int(input())
y = int(input())
somaImpar = 0
if y < x:
    x, y = y, x
i = x+1
while i < y:
    if i % 2 != 0:
        somaImpar += i
    i += 1
print(somaImpar)

