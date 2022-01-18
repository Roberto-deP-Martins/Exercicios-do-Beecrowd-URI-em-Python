numero = int(input())
lista = []
while len(lista) != 6:
    if numero % 2 != 0:
        lista.append(numero)
    numero += 1
for i in lista:
    print(i)