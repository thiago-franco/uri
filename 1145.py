x, y = [int(z) for z in input().split()]
i = 1
while i < y:
    s = ''
    for j in range(x):
        s += str(i+j) + ' '
    print(s.strip())
    i += x
    
