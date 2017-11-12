v = [float(x) for x in input().split()]
v.sort(reverse=True)
a = v[0]
b = v[1]
c = v[2]

if a >= b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2 == b**2+c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2+c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2+c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
