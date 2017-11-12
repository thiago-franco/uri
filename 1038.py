x = [int(a) for a in input().split()]
cod = x[0]
qtd = x[1]
dic = {1:4.0, 2:4.5, 3:5, 4:2, 5:1.5}
if cod in dic.keys() and qtd >= 0:
    total = dic[cod]*qtd
else:
    total = 0
print("Total: R$ %.2f" % total)
