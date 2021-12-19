a= input()

vet = []
for i in range(int(a)):
	x = int(input())
	vet.append(x)
respostas=[]
for i in range(int(a)):
    respostas.append(0)

if(int(a)==1):
    respostas[0]=vet[0]
    print("aqui?")
    # print(vet[0])
if(int(a)==2):
    respostas[0]=vet[0]+vet[1]
    # print()
    respostas[1]=vet[0]+vet[1]
    # print(vet[0]+vet[1])
if(int(a)>2):
    b=1
# c=1
 
    respostas[0]= vet[0]+vet[1]
    while(b <(int(a)-1)):
        
        respostas[b]= vet[b+1]+vet[b]+vet[b-1]
        b=b+1    
    respostas[int(a)-1]= vet[int(a)-2]+vet[int(a)-1]
for i in respostas:
    print(i)