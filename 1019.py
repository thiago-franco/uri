segundos = int(input())
minutos = segundos/60
horas = minutos/60
h = minutos//60
minutos = (horas % 60)%1*60
m = minutos//1
s = round((minutos % 60)%1*60)

print("%d:%d:%d" % (h, m, s))


