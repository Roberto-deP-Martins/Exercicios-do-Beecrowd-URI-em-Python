maximo = int(input())
inicio = 0
for i in range(1,maximo + 1):
    inicio += 1
    if inicio % 2 == 0:
        print('{}^2 = {}'.format(inicio, inicio ** 2))
