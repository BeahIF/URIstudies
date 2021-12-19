a = input()
matriz=[]
soma=0
for i in range(12):
    aux_matrix=[]
    for j in range(12):
        aux_matrix.append(float(input()))
    matriz.append(aux_matrix) 
j=0
for i in range(11):
    for j in range(11-i):
    
        soma= soma+matriz[i][j]
if(a=='M'):
   soma = soma / 66.0
print("{0:.1f}".format(soma))