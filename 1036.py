from math import sqrt

x = [float(a) for a in input().split()]
A = x[0]
B = x[1]
C = x[2]
delta = B**2 - 4 * A * C
if delta < 0 or A == 0:
    print("Impossivel calcular")
else:
    r1 = (-B + sqrt(delta))/(2*A)
    r2 = (-B - sqrt(delta))/(2*A)
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)
