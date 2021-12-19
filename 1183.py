a = input()
matriz=[]
for i in range(12):
    aux_matrix=[]
    for j in range(12):
        aux_matrix.append(float(input()))
    matrix.append(aux_matrix) 
j=1
if(a=='S'):
    for i in range(12):
        j=i+1
        while(j<12):
            soma= soma+matrix[i][j]
#( 144-12) /2
else:
    media = soma / 66.0