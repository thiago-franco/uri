alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def automato(string):
    estado = 1
    for s in string:
        if estado == 1 and s in alfabeto:
            estado = 2
        elif estado == 1:
            estado = 4
        elif estado == 2 and s in alfabeto:
            estado = 2
        elif estado == 2 and s == '.':
            estado = 3
        elif estado == 2:
            estado = 4
        elif estado == 3:
            estado = 4
    if estado == 2 or estado == 3:
        return True
    return False

while True:
    try:
        palavras = input().split()
        totalLetras = 0
        totalPalavras = 0
        for p in palavras:
            if automato(p):
                totalLetras += len(p)
                if p[len(p)-1] == '.':
                    totalLetras -= 1
                totalPalavras += 1
        media = 0
        if totalPalavras > 0:
            media = totalLetras//totalPalavras
        if media <= 3:
            print(250)
        elif media in [4,5]:
            print(500)
        else:
            print(1000)
    except:
        break

        
            
