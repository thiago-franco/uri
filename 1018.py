x = int(input())
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0
print(x)
sign = 1
if x < 0:
    x = x * -1
    sign = -1
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
while x - 1 >= 0:
    n1 = n1 + 1
    x = x - 1
print("%d nota(s) de R$ 100,00" % (n100*sign))
print("%d nota(s) de R$ 50,00" % (n50*sign))
print("%d nota(s) de R$ 20,00" % (n20*sign))
print("%d nota(s) de R$ 10,00" % (n10*sign))
print("%d nota(s) de R$ 5,00" % (n5*sign))
print("%d nota(s) de R$ 2,00" % (n2*sign))
print("%d nota(s) de R$ 1,00" % (n1*sign))
