comprimento = int(input())
alturas = []
cheios=0
for i in range(comprimento):
    alturas.append(int(input()))
    # fica cheio dependendo do tamanho das alturas do lado
cheios=0
maior = max(alturas)

for i in range(comprimento):
    if(i==0):
        print("no primeiro")
    #  esse caso nao enche
        cheios = cheios
    elif(i == comprimento-1):
#esse caso nao enche
        print("no ultimo")
        cheios = cheios
    else:
        if(maior == alturas[i]):
            print("nos altos")
            cheios = cheios
        else:
            meio =alturas[i]
            esquerda = alturas[i-1]
            direita = alturas[i+1] 
            if(direita > meio or direita > esquerda):
                cheios = cheios +1
            elif(direita > meio and esquerda == meio):
                cheios = cheios +1
            else:
                if(direita == meio and esquerda == meio):
                    cheios =cheios+1
                elif(direita < meio or direita < esquerda):
                    cheios = cheios+1
print(cheios)