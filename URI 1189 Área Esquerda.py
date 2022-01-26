def obterMedia():  # Faz a média
    media = sum(area) / len(area)
    return media


def obterArea():
    finalRange = 0  # Índice final da lista
    inicioRange = 0  # Índice inicial da lista
    numLinha = 1  # Linha dá qual se está obtendo valores
    area = []  # Lista com todos os valores da área
    while numLinha <= 10:  # Se usa conteúdo da área composta por 10 das 12 linhas da matriz
        # Até a linha número 5, o final do intervalo segue aumentando,
        # da 6 em diante, ele passa a diminuir, espelhando o comportamento das 5 anteriores
        if numLinha <= 5:  # Até quinta linha
            while numLinha <= 5:  # Segue o comportamento desse loop até a quinta linha
                # Pega os valores presentes no intervalo atual dentro da lista atual e os adiciona à lista da diagonal
                for t in matriz[numLinha][inicioRange:finalRange + 1]:
                    area.append(t)
                finalRange += 1  # Move final do intervalo, seguindo a figura (linha 1 - final 0, linha 2 - final 1,...)
                numLinha += 1  # Avança a linha da qual se está obtendo valores
        else:  # Quinta linha em diante
            while numLinha <= 10:   # Segue o comportamento desse loop até a décima linha
                # Pega os valores presentes no intervalo atual dentro da lista atual e os adiciona à lista da diagonal
                finalRange -= 1  # Move o final do intervalo, seguindo a figura (linha 6 - final 4, l 7 - f 3,...)
                for t in matriz[numLinha][inicioRange:finalRange + 1]:
                    area.append(t)
                numLinha += 1  # Avança a linha da qual se está obtendo valores
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
