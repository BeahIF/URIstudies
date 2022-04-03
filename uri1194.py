#Para cada sub-árvore, a raiz é o primeiro elemento do subvetor em pré-ordem, 
# um elemento do meio (que divide o vetor em filhos direitos e esquerdos) em in-ordem,
#  e o último elemento do subvetor em pós-ordem.
#versao para expressões matematicas
def infixToPostfix(l):
    stack=[]
    ps=""
    p={"+":3,"-":3,"x":2,"/":2,"^":1}
    print(p)
    for i in l:
        if i in p:
            while len(stack)!=0 and stack[-1]!="(" and p[stack[-1]]<=p[i]:
                print("primeiro while")
                ps+=stack[-1]
                print(ps)
                stack.pop(-1)
                print(stack)
            stack.append(i)
            print(stack)
        elif i=="(":
            stack.append("(")
        elif i==")":
            while len(stack)!=0 and stack[-1]!="(":
                print("segundo while")
                ps+=stack[-1]
                print(ps)
                stack.pop(-1)
                print(stack)
            if len(stack)!=0:
                stack.pop(-1)
                print(stack)
        else:
            ps+=i
    while len(stack)!=0:
        ps+=stack.pop(-1)
        print(ps)
    return ps

a = input()
i=0
while(i<int(a)):
    cases = input()
    cases = cases.split()
    print(cases)
    postfix= infixToPostfix(cases[1])
    print(postfix)
    i=i+1
#versao correta 


current =0
result=""

def infixToPostfix(pre, infix, p, q):
    print("chega aqui ")
    #p=0 e q=2
    print("p"+str(p))
    print("q"+str(q))
    if(int(p)<=int(q)):
        print("entreu no if")
        global current
        current=current+1
        print("current"+str(current))
        print(pre[current])
        print(infix.find(pre[current]))
        pos = infix.find(pre[current])
        infixToPostfix(pre, infix, p, pos-1)
        print("passei aqui")
        print("q"+str(q))
        infixToPostfix(pre, infix, pos+1, q)
        global result
        print("pos"+str(pos))
        result = result +infix[pos]
        print(infix[pos])
        print(result)
        return result
test = input()

i=1
while(i<=int(test)):
    result=""
    current = -1
    # n = input()
    # pre = input()
    # infix = input()
    cases = input()
    cases = cases.split()
    # print(cases[0])
    # print(cases[1])
    print(infixToPostfix(cases[1], cases[2], 0, int(int(cases[0])-1)))
    # print(endl)
    # print(postfix)
    i=i+1