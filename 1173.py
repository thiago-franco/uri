x = int(input())
v = [x]
for i in range(1,10):
    v.append(v[i-1]*2)
for i in range(0, len(v)):
    print("N[%d] = %d" % (i,v[i]))
