
while True:
    M, N = map(int, input().split())
    if (M == N == 0):
        break

    soma = M + N
    soma = str(soma)
    soma = soma.replace('0', '')
    soma = int(soma)
    print(soma)
    