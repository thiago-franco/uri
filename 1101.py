while True:
    m, n = [int(x) for x in input().split()]
    if m <= 0 or n <= 0:
        break
    if m > n:
        m,n = n,m
    s = range(m,n+1)
    t = ''
    for i in s:
        t += str(i) + ' '
    t += 'Sum=' + str(sum(s))
    print(t)
