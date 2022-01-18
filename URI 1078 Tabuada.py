valor = int(input())
inicio = 0
for i in range(10):
    inicio += 1
    print('{} x {} ='.format(inicio, valor), inicio * valor)