v = []
for i in range(10):
    v.append(int(input()))
v = [x if x > 0 else 1 for x in v]
for i in range(0, len(v)):
    print("X[%d] = %d" % (i, v[i]))
