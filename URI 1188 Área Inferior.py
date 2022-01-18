def obterMedia():  # Faz a média
    media = sum(area) / len(area)
    return media


def obterArea():
    finalRange = 10  # Índice final da lista
    inicioRange = 1  # Índice inicial da lista
    numLinha = 11  # Linha dá qual se está obtendo valores
    area = []  # Lista com todos os valores da área
    while numLinha >= 7:  # Se usa conteúdo da área composta pelas 4 linhas inferiores
        # Pega os valores presentes no intervalo atual dentro da lista atual e os adiciona à lista da diagonal
        for t in matriz[numLinha][inicioRange:finalRange + 1]:
            area.append(t)
        inicioRange += 1  # Move o início do intervalo, seguindo a figura (linha 11 - início 1, linha 10 - início 2,...)
        finalRange -= 1  # Move o final do intervalo, seguindo a figura (linha 11 - final 10, linha 10 - final 9,...)
        numLinha -= 1  # Avança a linha da qual se está obtendo valores
    return area

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

area = obterArea()  # Obtém a área
if operacao == 'S':
    soma = sum(area)
    print('%.1f' % soma)
elif operacao == 'M':
    media = obterMedia()
    print('%.1f' % media)
