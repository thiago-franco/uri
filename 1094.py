n = int(input())
cobaias = [0,0,0]
for i in range(n):
    x, t = input().split()
    if t == 'C':
        cobaias[0] += int(x)
    elif t == 'R':
        cobaias[1] += int(x)
    elif t == 'S':
        cobaias[2] += int(x)
total = cobaias[0]+cobaias[1]+cobaias[2]
print("Total: %d cobaias" % total)
print("Total de coelhos: %d" % cobaias[0])
print("Total de ratos: %d" % cobaias[1])
print("Total de sapos: %d" % cobaias[2])
pc = int(cobaias[0])/int(total)*100
pr = int(cobaias[1])/int(total)*100
ps = int(cobaias[2])/int(total)*100
print("Percentual de coelhos: %.2f %%" % pc)
print("Percentual de ratos: %.2f %%" % pr)
print("Percentual de sapos: %.2f %%" % ps)
