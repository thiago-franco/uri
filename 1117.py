v = []
while True:
    n = float(input())
    if n >= 0 and n <= 10:
        v.append(n)
        if len(v) == 2:
            break
    else:
        print("nota invalida")
m = sum(v)/2
print("media = %.2f" % m)
