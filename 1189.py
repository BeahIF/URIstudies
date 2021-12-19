a = input()
matrix=[]
soma=0
for i in range(12):
    aux_matrix=[]
    for j in range(12):
        aux_matrix.append(float(input()))
    matrix.append(aux_matrix) 
j=1
i=0
if(a=='S'):
#     for i in range(10):
#         if(i<=5):
#             j=0
#             while(j<i):
#                 soma= soma+matrix[i][j]
#                 j=j+1
#         else:
#             j=0
#             while(j<11-i):
#                 soma= soma+matrix[i][j]
#                 j=j+1
    for i in range(5):
        for j in range(1+i,11-i):
            soma=soma+matrix[j][i]
        

#( 144-12) /2
else:
    soma = soma / ((144-12-12)/4)
print("{0:.2f}".format(soma))