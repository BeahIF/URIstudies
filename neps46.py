
def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

linha = read_line()

lista = linha.split(" ")
l,r,d = lista[0], lista[1], lista[2]
if((int(r)>50)and(int(l)<int(r))and(int(r)>int(d))):
    print("S")
else:
    print("N")