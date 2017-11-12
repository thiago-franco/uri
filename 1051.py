sal = float(input())

if sal <= 2000:
    print("Isento")
else:
    taxa = 0
    incide = sal - 2000
    if sal >= 2000.01 and sal <= 3000:
        taxa = incide * 0.08
    incide = sal - 3000 
    if sal >= 3000.01 and sal <= 4500:
        taxa = incide * 0.18 + 80
    incide = sal - 4500
    if sal >= 4500.01:
        taxa = incide * 0.28 + 270 + 80
    print("R$ %.2f" % taxa)
