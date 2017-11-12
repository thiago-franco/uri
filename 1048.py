x = float(input())

p = 0

if x > 0 and x <= 400:
    p = 0.15
elif x >= 400.01 and x <= 800:
    p = 0.12
elif x >= 800.01 and x <= 1200:
    p = 0.10
elif x >= 1200.01 and x <= 2000:
    p = 0.07
elif x > 2000:
    p = 0.04

print("Novo salario: %.2f" % (x+x*p))
print("Reajuste ganho: %.2f" % (x*p))
print("Em percentual: %d %%" % (p*100))
