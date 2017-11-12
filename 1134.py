combs = [0,0,0]
while True:
    c = int(input())
    if c == 4:
        break
    if c not in (1,2,3):
        continue
    combs[c-1] += 1
print("MUITO OBRIGADO")
print("Alcool: %d" % combs[0])
print("Gasolina: %d" % combs[1])
print("Diesel: %d" % combs[2])
