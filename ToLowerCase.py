i=0
result=''
s = "Hello"
while(i<len(s)):
    chrWord=ord(s[i])
    print(chrWord)
    if(chrWord <=  ord('Z') and chrWord>= ord('A')):
        result =  result+chr(chrWord - ord('A') +ord('a'))
    i=i+1
    
print(result)