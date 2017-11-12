n = int(input())
for i in range(n):
    x, y = [int(x) for x in input().split()]
    if x > y:
        x, y = y, x
    impares = [z for z in range(x+1,y) if z%2 != 0]
    print(sum(impares))
