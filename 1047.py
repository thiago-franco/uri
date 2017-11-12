hi, mi, hf, mf = [int(x) for x in input().split()]

i = mi + 60*hi
f = mf + 60*hf

if i >= f:
    d = 24*60 - i + f
else:
    d = f - i
h = d//60
m = round((d%60), 2)

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))
