qtdTestes = int(input())
lista = []
dentro = []
fora = []
for i in range(qtdTestes):
    x = int(input())
    lista.append(x)
for i in lista:
    if 10 <= i <= 20:
        dentro.append(i)
    else:
        fora.append(i)
print(len(dentro), 'in')
print(len(fora), 'out')
