from math import sqrt

n = int(input())
fibonacci = (((1 + sqrt(5))/2)**n - ((1 - sqrt(5))/2)**n)/sqrt(5)
print("%.1f" % fibonacci)
