from math import ceil

# 1ª variável diz quantidade por linha e quanto os números aumentam por linha e a 2ª em que número encerra
numPorLinha, fim = map(int, input().split())
lista = []
listaFinal = []
t = 0  # Varíavel será usada para adicionar os números da primeira linha
linhas = 0  # Variável usada para contar quantas linhas foram geradas
indice = 0  # Usado para manipulação de lista
for i in range(numPorLinha):  # Ocorre até gerar todos os números da primeira linha (determinando tbm tamanho delas)
    t += 1  # Gera os primeiros números (1, 2, 3, 4, 5, ...)
    lista.append(t)  # Adiciona esses números à lista
print(*lista)  # Imprime a primeira linha
# Ceil arredonda para cima a divisão, garantindo que se gerem todas as linhas necessárias para se chegar ao num final
# A divisão dá o número de linhas necessárias para se chegar ao número final, subtrai-se 1 pois já se gerou a primeira
while linhas < (ceil(fim / numPorLinha) - 1):
    linhas += 1  # Adiciona ao número de linhas
    lista = [i + numPorLinha for i in lista]  # Faz as somas (pelo número digitado) sobre os números da lista
    # Ao se chegar na última linha, verifica-se a posição do último valor para se gerar apenas ele e seus antecedentes
    if linhas == (ceil(fim / numPorLinha) - 1):
        for i in lista:
            if i == fim:  # Verifica se o número final está presente na linha
                posicao = lista.index(i)  # Adquire sua posição
                for i in range(posicao + 1):  # Loop até chegar no valor final
                    listaFinal.append(lista[indice])  # Gera a lista com os elementos da linha final
                    indice += 1
                print(*listaFinal)
    else:  # Imprime todas as linhas exceto a final
        print(*lista)
