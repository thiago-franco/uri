x = int(input())
y = int(input())
if x > y:
    x,y = y,x
m = [z for z in range(x,y+1) if z%13 != 0]
print(sum(m))

