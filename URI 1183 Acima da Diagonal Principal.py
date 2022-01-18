# Constrói as 12 linhas que compõem a matriz e, por consequência, a matriz em si.
def obterMedia(vetor):  # Faz a média
    resultado = sum(vetor) / len(vetor)
    return resultado


def constroiMatriz():
    matriz = []
    while len(matriz) < 12:  # Roda até haverem 12 linhas
        linha = []
        for i in range(12):  # Roda até que a linha tenha 12 elementos
            linha.append(float(input()))  # Adiciona o que o usuário digitar
        matriz.append(linha)  # Adiciona a linha à matriz
    return matriz


def obterDiagonal():
    finalRange = 11  # Índice final da lista
    inicioRange = 1  # Índice inicial da lista
    diagonal = []  # Lista com todos os valores da diagonal
    for linha in range(11):  # Se usa conteúdo da diagonal composta pelas 10 linhas superiores
        # Pega os valores presentes no intervalo atual dentro da lista atual e os adiciona à lista da diagonal
        for valor in matriz[linha][inicioRange:finalRange + 1]:
            diagonal.append(valor)
        inicioRange += 1  # Move o início do intervalo, pois é diagonal (linha 0 - início 1, linha 1 - inicio 2,...)
    return diagonal


# Matrizes muitas vezes são representadas por uma grade x por y
# Diante dessa representação, em Python as linhas seriam elementos ([0],[1],[2]...) da matriz
# Colunas seriam [y] de cada elemento  da matriz (matriz[0][0],[1][[0],[2][0]...)

operacao = input()  # Operação que será realizada
matriz = constroiMatriz()
diagonal = obterDiagonal()
if operacao == 'S':
    soma = sum(diagonal)
    print('%.1f' % soma)
elif operacao == 'M':
    media = obterMedia(diagonal)
    print('%.1f' % media)
