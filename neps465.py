area= (160*70)/2
# 5600
altura=70
b=int(input())
t=int(input())
novaarea= b*altura
# 4900
novaarea= novaarea+((altura*(t-b))/2)
print(novaarea)
# 4650

if(novaarea>area):
    print(1)
elif(novaarea==area):
    print(0)
else:
    print(2)
