n = int(input())
for i in range(n):
    a,b,c = [float(x) for x in input().split()]
    media = (2*a+3*b+5*c)/10
    print("%.1f" % media)

