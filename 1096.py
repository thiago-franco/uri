i = 1
j = 7
while i <= 9:
    print("I=%d J=%d" % (i,j))
    j -= 1
    if j == 4:
        j = 7
    if j == 7:
        i += 2
