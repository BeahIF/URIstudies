total = int(input())
cidades= int(input())
vet=[]

for i in range(cidades):
    vet.append(int(input()))
print(vet)
estradas = []
c=0
d=0
i=1

for d in vet:
        print("D")
        print(d)
        
        while(i<total):
        # for i in range(total):
            print("i")
            print(i)
  
            if(d==i):
                estradas.append(1)
                i=total
            else:
                estradas.append(0)
            i=i+1
        i=d+1
print(i)
while(i<=total):
    estradas.append(0)
    i=i+1
print(estradas)
menor=0
# indo para a direita
# print(estradas[c])
while(c<total):
    if(estradas[c]!=0):
        posicao=c+1
        print(estradas[c])
        menor=c+1
        c=total
    c=c+1
print("menor")
print(menor)
c=posicao
e=posicao
# c=estradas[c-1]
# e=estradas[c-1]
print(e)
c=c+1
distancia=0
# e=e+1
while(e<total):
    if(estradas[e]==0):
        distancia = distancia+1
    if(estradas[e]==1):
        e=total
        # c=c+1
    e=e+1
print("distancia")
print(distancia)
if(distancia<menor):
    menor=distancia
menor = (distancia+1)/2
print(menor)
