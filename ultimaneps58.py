comprimento = int(input())
alturas = []
cheios=0
for i in range(comprimento):
    alturas.append(int(input()))
cheios=0

maiores = max(alturas)
for i in range(comprimento):
    if(i!=0 and (i != comprimento-1) and ((alturas[i]<= maiores) and 
        (alturas[i] < max(alturas[i:]))
        and (alturas[i] < max(alturas[:i])))):
        
 
      
            cheios = cheios+1

print(cheios)