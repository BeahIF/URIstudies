def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()
tam=input()
a=0
vet = []

numeros = read_line()
n = numeros.split(' ')
menor = int(n[0])
posicao=0
for i in range(int(tam)):
    if(int(n[i])<menor):
        menor=int(n[i])
        posicao=i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')
