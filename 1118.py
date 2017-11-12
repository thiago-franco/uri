while True:
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
    c = ''
    while c not in (1,2):
        print("novo calculo (1-sim 2-nao)")
        c = int(input())
    if c == 2:
        break
    
    

