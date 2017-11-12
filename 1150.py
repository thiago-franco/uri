x = int(input())
z = -999999999999
while True:
    i = int(input())
    if i > x:
        z = i
        break
a = x
c = 1
while a < z:
    a += x+c
    c += 1
print(c)
