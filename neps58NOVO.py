comprimento = int(input())
alturas = []
cheios=0
for i in range(comprimento):
    alturas.append(int(input()))
    # fica cheio dependendo do tamanho das alturas do lado
cheios=0
maiorDireita = []
maiorEsquerda=[]
i = 0
for i in range(comprimento):
    maiorDireita.append(alturas[i])    
i=comprimento-1
while(i >= 0):
    maiorEsquerda.append(alturas[i]) 
    i=i-1
print(maiorDireita)
print(maiorEsquerda)
print(alturas)
i=0
for i in range(comprimento):
    if(min(maiorEsquerda[i], maiorDireita[i]) >= alturas[i]):
        cheios += 1
print(cheios)