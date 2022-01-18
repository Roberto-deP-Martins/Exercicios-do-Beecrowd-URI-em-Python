lista = []
for i in range(5):
    entrada = int(input())
    if entrada % 2 == 0:
        lista.append(entrada)
print(len(lista), 'valores pares')