i = 1
j = i+6
while i <= 9:
    print("I=%d J=%d" % (i,j))
    j -= 1
    if j == i+3:
        i += 2
        j = i+6
