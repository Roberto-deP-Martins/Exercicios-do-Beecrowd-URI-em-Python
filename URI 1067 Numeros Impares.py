numero = int(input())
inicio = 0
impares = []
for i in range(numero):
    inicio += 1
    if inicio % 2 != 0:
        impares.append(inicio)
for i in impares:
    print(i)