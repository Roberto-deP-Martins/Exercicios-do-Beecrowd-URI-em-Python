def obterMedia():  # Faz a média
    media = sum(diagonal) / len(diagonal)
    return media


def obterDiagonal():
    finalRange = 11  # Índice final da lista
    inicioRange = 11  # Índice inicial da lista
    numLinha = 1  # Linha dá qual se está obtendo valores
    diagonal = []  # Lista com todos os valores da diagonal
    while numLinha <= 11:  # Se usa conteúdo da diagonal composta pelas 11 linhas inferiores
        # Pega os valores presentes no intervalo atual dentro da lista atual e os adiciona à lista da diagonal
        for t in matriz[numLinha][inicioRange:finalRange + 1]:
            diagonal.append(t)
        inicioRange -= 1  # Move o início do intervalo, pois é diagonal (linha 1 - início 11, linha 2 - início 10,...)
        numLinha += 1  # Avança a linha da qual se está obtendo valores
    return diagonal

# Matrizes muitas vezes são representadas por uma grade x por y
# Diante dessa representação, em Python as linhas seriam elementos ([0],[1],[2]...) da matriz
# Colunas seriam [y] de cada elemento  da matriz (matriz[0][0],[1][[0],[2][0]...)


matriz = []
operacao = input()  # Operação que será realizada

# Constrói a matriz
while len(matriz) < 12:  # Roda até haverem 12 linhas
    linha = []
    for i in range(12):  # Roda até que a linha tenha 12 elementos
        linha.append(float(input()))  # Adiciona o que o usuário digitar
    matriz.append(linha)  # Adiciona a linha à matriz

diagonal = obterDiagonal()  # Obtém a diagonal
if operacao == 'S':
    soma = sum(diagonal)
    print('%.1f' % soma)
elif operacao == 'M':
    media = obterMedia()
    print('%.1f' % media)
