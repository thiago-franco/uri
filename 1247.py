from sys import stdin
from math import sqrt

for linha in stdin:
    d, vf, vg = [int(x) for x in linha.split()]
    h = sqrt(d**2 + 12**2)
    tf = 12/vf
    tg = h/vg
    if tf < tg:
        print("N")
    else:
        print("S")
