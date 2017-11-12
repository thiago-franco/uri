n = int(input())
for i in range(n):
    x, y = [int(z) for z in input().split()]
    try:
        d = x/y
        print(d)
    except:
        print("divisao impossivel")
