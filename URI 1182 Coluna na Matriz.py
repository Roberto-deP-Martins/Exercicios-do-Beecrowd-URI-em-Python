def obterMedia(coluna):  # Faz a média
    resultado = sum(coluna) / 12
    return resultado


# Constrói as 12 linhas que compõem a matriz e, por consequência, a matriz em si.
def constroiMatriz():
    matriz = []
    while len(matriz) < 12:  # Roda até haverem 12 linhas
        linha = []
        for i in range(12):  # Roda até que a linha tenha 12 elementos
            linha.append(float(input()))  # Adiciona o que o usuário digitar
        matriz.append(linha)  # Adiciona a linha à matriz
    return matriz


# Matrizes muitas vezes são representadas por uma grade x por y
# Diante dessa representação, em Python as linhas seriam elementos ([0],[1],[2]...) da matriz
# Colunas seriam [y] de cada elemento  da matriz (matriz[0][0],[1][[0],[2][0]...)

# Parâmetros
numColuna = int(input())  # Coluna com a qual será realizada a operação
operacao = input()  # Operação que será realizada
matriz = constroiMatriz()

# Constrói a lista que contém todos os elementos da coluna
coluna = []
for t in matriz:  # t é cada linha da matriz (que no Python seria cada uma das listas no interior da matriz)
    coluna.append(t[numColuna])  # Adiciona à lista da coluna o elemento presente na coluna 5 para cada linha

# Realiza as operações
if operacao == 'S':
    soma = sum(coluna)
    print('%.1f' % soma)
elif operacao == 'M':
    media = obterMedia(coluna)
    print('%.1f' % media)
