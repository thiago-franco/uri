while True:
    m, n = [int(x) for x in input().split()]
    if m == n:
        break
    if m < n:
        print("Crescente")
    else:
        print("Decrescente")
