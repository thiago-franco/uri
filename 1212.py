while True:
    x,y = [z for z in input().split()]
    if x == '0' and y == '0':
        break
    if int(x) < int(y):
        x,y = y,x
    x = x[::-1]
    y = y[::-1]
    for i in range(len(x)-len(y)):
        y += '0'
    z = []
    qtdVai1 = 0
    vai1 = 0
    for i,k in enumerate(x):
        z.append(int(x[i]) + int(y[i]) + vai1)
        if int(z[i]) > 9:
            z[i] = int(z[i])-10
            vai1 = 1
            qtdVai1 += 1
        else:
            vai1 = 0
    if vai1 == 1:
        z.append(1)
    z.reverse()
    if qtdVai1 == 0:
        print("No carry operation.")
    elif qtdVai1 == 1:
        print("%d carry operation." % qtdVai1)
    else:
        print("%d carry operations." % qtdVai1)
        
