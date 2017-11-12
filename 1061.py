def entrarData():
    v = list()
    v.extend([int(x) for x in input().split()[1]])
    v.extend([int(x) for x in input().split(' : ')])
    return v

def paraSegundos(data):
    segundos = 0
    segundos += data[0]*24*60*60
    segundos += data[1]*60*60
    segundos += data[2]*60
    segundos += data[3]
    return segundos

def paraData(tempo):
    data = list()
    total = tempo/60/60/24
    dias = total//1
    horas = (total%1*24)//1
    minutos = ((total%1*24)%1*60)//1
    segundos = round(((total%1*24)%1*60)%1*60)//1
    data.append(dias)
    data.append(horas)
    data.append(minutos)
    data.append(segundos)
    if data[3] == 60:
        data[2] += 1
        data[3] = 0
    if data[2] == 60:
        data[1] += 1
        data[2] = 0
    if data[1] == 24:
        data[0] += 1
        data[1] = 0
    return data

inicio = entrarData()
fim = entrarData()
diferenca = paraSegundos(fim) - paraSegundos(inicio)
duracao = paraData(diferenca)
if duracao[0] + duracao[1] + duracao[2] + duracao[3] == 0:
    duracao[2] += 1 #Duracao minima de 1 minuto
print("%d dia(s)" % duracao[0])
print("%d hora(s)" % duracao[1])
print("%d minuto(s)" % duracao[2])
print("%d segundo(s)" % duracao[3])
