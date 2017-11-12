i = 0
while i <= 2:
    j = i
    for n in range(3):
        j += 1
        s = 'I='
        if i % 1 > 0.9:
            i = round(i)
        if i % 1 == 0:
            s += '%d'
        else:
            s += '%.1f'
        s += ' J='
        if j % 1 == 0:
            s += '%d'
        else:
            s += '%.1f'
        print(s % (i,j))
    i += 0.2
