lista = []
for i in range(6):
    numero = float(input())
    if numero > 0:
        lista.append(numero)
print(len(lista), 'valores positivos')