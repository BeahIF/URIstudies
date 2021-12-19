

a=0
par=[]
impar=[]
while(a<10):
    b= input()
    
    if(int(b)%2==0):
        par.append(b)
    else:
        impar.append(b)
    a=a+1
a=0
while(a<10):
    print(par[a])
a=0
while(a<10):
    print(impar[a])
   
