s = ["h","e","l","l","o"]
# i=0
# res=[]
# print(len(s))
# tam=len(s)
# while(i<len(s)):
#     print(s[tam-1])
#     res.append(s[tam-1])
#     i=i+1
#     tam=tam-1

# print(res)
# this first try didn't work because they say         :rtype: None "Do not return anything, modify s in-place instead".
# which means that I shouldn't use a new vector, I should swap the original vector as:
esquerda =0
direita= len(s)-1
while(esquerda<direita):
    i=s[esquerda]
    s[esquerda]=s[direita]
    s[direita]=i
    esquerda=esquerda+1
    direita=direita-1