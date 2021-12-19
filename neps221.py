def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()
linha=read_line()
linha=linha.split(' ')
n,p=linha[0], linha[1]
vencedores=0
for i in range(int(n)):
    linha=read_line()
    linha=linha.split(' ')
    if((int(linha[0])+int(linha[1]))>=int(p)):
        vencedores = vencedores+1
print(vencedores)