par = []
impar = []
for i in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
    if len(par) == 5:
        for idx, p in enumerate(par):
            print("par[%d] = %d" % (idx,p))
        par.clear()
    if len(impar) == 5:
        for idx, ip in enumerate(impar):
            print("impar[%d] = %d" % (idx,ip))
        impar.clear()
if len(impar) > 0:
    for idx, ip in enumerate(impar):
        print("impar[%d] = %d" % (idx,ip))
if len(par) > 0:
    for idx, p in enumerate(par):
        print("par[%d] = %d" % (idx,p))
    
