lista = []
for i in range(100):
    numero = int(input())
    lista.append(numero)
listaOrganizada = sorted(lista)
print(listaOrganizada[-1])
print(lista.index(listaOrganizada[-1]) + 1)  # Imprime a posição do maior número na lista original + 1
