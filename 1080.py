m = -999999999999
p = -1
for i in range(1,101):
    n = int(input())
    if n > m:
        m = n
        p = i
print(m)
print(p)
