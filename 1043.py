a, b, c = [float(x) for x in input().split()]

c1 = abs(b-c) < a < b+c
c2 = abs(a-c) < b < a+c
c3 = abs(a-b) < c < a+b

if c1 and c2 and c3:
    p = a+b+c
    print("Perimetro =", p)
else:
    area = c*(a+b)/2
    print("Area =", round(area,1))
