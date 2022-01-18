def obterMedia(indice):  # Faz a média
    media = sum(matriz[indice]) / 12
    return media

# Matrizes muitas vezes são representadas por uma grade x por y
# Diante dessa representação, em Python as linhas seriam elementos ([0],[1],[2]...) da matriz
# Colunas seriam [y] de cada elemento  da matriz (matriz[0][0],[1][[0],[2][0]...)


matriz = []
numLinha = int(input())  # Linha com a qual será realizada a operação
operacao = input()  # Operação que será realizada
while len(matriz) < 12:  # Roda até haverem 12 linhas
    linha = []
    for i in range(12):  # Roda até que a linha tenha 12 elementos
        linha.append(float(input()))  # Adiciona o que o usuário digitar
    matriz.append(linha)  # Adiciona a linha à matriz
if operacao == 'S':
    soma = sum(matriz[numLinha])
    print('%.1f' % soma)
elif operacao == 'M':
    media = obterMedia(numLinha)
    print('%.1f' % media)
