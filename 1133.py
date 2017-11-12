x = int(input())
y = int(input())
if x > y:
    x,y = y,x
[print(z) for z in range(x+1,y) if z%5 == 3 or z%5 == 2]

