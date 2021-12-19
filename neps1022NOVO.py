total = int(input())
cidades= int(input())
vet=[]
distancia=0
distanciaMenor=0
for i in range(cidades):
    vet.append(int(input()))
print(vet)
vet.sort()
print(vet)
# caso inicio
i=0

for i in range(cidades):
    if(i==0):
        esquerda = vet[i]
        print(esquerda)
        direita = ((vet[i] + vet[i+1])/2 )-vet[i]
        print(direita)
        distancia = esquerda + direita
        print(distancia)
        distanciaMenor = distancia
    elif(i == cidades-1):
        esquerda = ((vet[i] + vet[i-1])/2)-vet[i-1]
        print(esquerda)
        direita = total-vet[i]
        print(direita)
        distancia = esquerda + direita
        print(distancia)
        distanciaMenor = min(distancia,distanciaMenor)
    else:
        esquerda = ((vet[i] + vet[i-1])/2)-vet[i-1]
        direita = ((vet[i]+ vet[i+1])/2)-vet[i]
        distancia =esquerda+direita
        distanciaMenor = min(distancia,distanciaMenor)
print("{0:.2f}".format(distanciaMenor))


# caso final

# caso meio
# a=0
# while(a<cidades):
#     distancias.append((vet[a]))
#     a=a+1
# b=cidades-2
# print(vet[cidades-1])
# while(b>0):
#     distancias.append((vet[cidades-1])-vet[b])
#     b=b-1
# c=0
# d=1
# while(c<cidades):
#     while(d<cidades):
#         distancias.append((vet[d])-(vet[c]))
#         d=d+1
#     c=c+1


