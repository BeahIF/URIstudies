a = int(input())
matriz=[]
for i in range(a):
    linha=list(map(int , input().split()))
    matriz.append(linha)

somas=[]

for i in range(a):

    somas.append(sum(matriz[i]))
for i in range(a):
    
    soma=0
    for j in range(a):

        soma = soma+matriz[j][i] 
    somas.append(soma)
# diagonal
soma=0
for i in range(a):
    soma=soma+matriz[i][i]
somas.append(soma)
j=0
soma=0
for i in range(a-1,-1,-1):
    
    soma=soma+matriz[j][i]
    j+=1

somas.append(soma)
print("-1" if len(list(set(somas))) > 1 else str(somas[0]))
