fatorial = int(input())  # Número do qual se quer o fatorial
posicaoFatorial = 0  # Quantos números do fatorial já foram processados
listaFatorial = []  # Lista com os valores multiplicados no fatorial
indice = 0
for i in range(fatorial):
    listaFatorial.append(fatorial - posicaoFatorial)
    posicaoFatorial += 1
for i in range(len(listaFatorial)):
    indice += 1
    listaFatorial[0] = listaFatorial[0] + listaFatorial[indice]
print(listaFatorial)