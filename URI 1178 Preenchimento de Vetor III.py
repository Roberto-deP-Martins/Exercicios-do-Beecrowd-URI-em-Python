x = float(input())
lista = [x]
for i in range(99):  # De 0 à 99
    x /= 2  # Segue produzindo a metade do número anterior (200/2 , 100/2, 50/2, 25/2, etc)
    lista.append(x)  # Põe na lista
for t in lista:  # Imprime cada item da lista
    print('N[{}] = {}'.format(lista.index(t), '%.4f' % t))
