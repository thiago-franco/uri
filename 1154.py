m = 0
t = 0
while True:
    x = int(input())
    if x < 0:
        break
    m += x
    t += 1
print("%.2f" % (m/t))
