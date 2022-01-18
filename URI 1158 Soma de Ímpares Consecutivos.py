qtdTestes = int(input())
for i in range(qtdTestes):  # Acontece o número de vezes determinado por qtdTestes
    x, y = map(int, input().split())  # Separa valores inteiros de uma mesma linha para x e y
    impares = []  # Lista para os ímpares
    while len(impares) != y:  # Repete até ter o número de ímpares determinado por y
        if x % 2 != 0:  # Verifica se é par
            impares.append(x)
            x += 1  # Vai somando 1 até ter o número de ímpares determinado por y
        else:
            x += 1
    print(sum(impares))
