v = []
for i in range(100):
    v.append(float(input()))
v = [(i, x) for i, x in enumerate(v) if x <= 10]
for i in v:
    print("A[%d] = %.1f" % (i[0], i[1]))
