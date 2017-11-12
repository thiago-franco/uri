n = int(input())
f = [0,1]
s = "0 1"
for i in range(2, n): # Os 2 primeiros termos já estão calculados
    nf = f[i-1] + f[i-2]
    f.append(nf)
    s += ' ' + str(nf)
print(s)
