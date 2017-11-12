while True:
    x = int(input())
    if x == 0:
        break
    s = ''
    for i in range(1, x+1):
        s += str(i) + ' '
    print(s.strip())
