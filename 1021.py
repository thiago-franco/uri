x = float(input())
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
m1 = 0
m50 = 0
m25 = 0
m10 = 0
m5 = 0
m01 = 0
sign = 1
if x < 0:
    x = x * -1
    sign = -1
print("NOTAS:")
while x - 100 >= 0:
    n100 = n100 + 1
    x = x - 100
while x - 50 >= 0:
    n50 = n50 + 1
    x = x - 50
while x - 20 >= 0:
    n20 = n20 + 1
    x = x - 20
while x - 10 >= 0:
    n10 = n10 + 1
    x = x - 10
while x - 5 >= 0:
    n5 = n5 + 1
    x = x - 5
while x - 2 >= 0:
    n2 = n2 + 1
    x = x - 2
print("%d nota(s) de R$ 100.00" % (n100*sign))
print("%d nota(s) de R$ 50.00" % (n50*sign))
print("%d nota(s) de R$ 20.00" % (n20*sign))
print("%d nota(s) de R$ 10.00" % (n10*sign))
print("%d nota(s) de R$ 5.00" % (n5*sign))
print("%d nota(s) de R$ 2.00" % (n2*sign))

print("MOEDAS:")
while x - 1 >= 0:    
    m1 = m1 + 1
    x = round(x - 1,2)
while x - 0.5 >= 0:
    m50 = m50 + 1
    x = round(x - 0.5,2)
while x - 0.25 >= 0:
    m25 = m25 + 1
    x = round(x - 0.25,2)
while x - 0.10 >= 0:
    m10 = m10 + 1
    x = round(x - 0.10,2)
while x - 0.05 >= 0:
    m5 = m5 + 1
    x = round(x - 0.05,2)
while x - 0.01 >= 0:
    m01 = m01 + 1
    x = round(x - 0.01,2)
print("%d moeda(s) de R$ 1.00" % (m1*sign))
print("%d moeda(s) de R$ 0.50" % (m50*sign))
print("%d moeda(s) de R$ 0.25" % (m25*sign))
print("%d moeda(s) de R$ 0.10" % (m10*sign))
print("%d moeda(s) de R$ 0.05" % (m5*sign))
print("%d moeda(s) de R$ 0.01" % (m01*sign))
