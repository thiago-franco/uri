def par(x):
    if x % 2 == 0:
        return True
    else:
        return False

def valorGolpe(p, b):
    v = (p[0] + p[1])/2
    if par(p[2]):
        v += b
    return v

instancias = int(input())

for i in range(instancias):
    b = int(input())
    dabriel = [int(x) for x in input().split()]
    guarte = [int(x) for x in input().split()]
    vgdabriel = (dabriel[0] + dabriel[1])/2
    vd = valorGolpe(dabriel, b)
    vg = valorGolpe(guarte, b)
    if vd > vg:
        print("Dabriel")
    elif vg > vd:
        print("Guarte")
    else:
        print("Empate")
