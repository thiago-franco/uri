from sys import stdin 
import math

g = 9.80665
pi = 3.14159

for linha in stdin:
    h = float(linha.replace('\n', ''))
    p1,p2 = [int(x) for x in input().split()]
    n = int(input())
    for i in range(n):
        a,v = [float(x) for x in input().split()]
        a = a*pi/180
        vx = v*math.cos(a)
        vy = v*math.sin(a)
        w = g*h/(v*v)
        t = (v/g)*(math.sin(a) + math.sqrt(math.sin(a)**2 + 2*w))
        x = vx*t
        if int(math.floor(x)) in range(p1,p2+1):
            print("%.5f -> DUCK" % x)
        else:
            print("%.5f -> NUCK" % x)
        
