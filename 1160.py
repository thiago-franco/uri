t = int(input())
for i in range(t):
    pa, pb, ga, gb = [float(x) for x in input().split()]
    i = 0
    while pa <= pb:
        pa += int(pa*(ga/100))
        pb += int(pb*(gb/100))
        i+= 1
        if i > 100:
            break
    if i > 100:
        print("Mais de 1 seculo.")
    else:
        print("%d anos." % i)
