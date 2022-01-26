# Gera as primeiras linhas antes do meio, em seguida a linha do meio, e por último, reverte as linhas antes do meio
while True:
    try:
        ordemDaMatriz = int(input())
        matrizTemp = []
        matriz = []
        # int(ordemDaMatriz / 2) arredonda para baixo a divisão da ordem da matriz (que dita o número de linhas), dessa
        # forma, gera-se apenas as linhas anteriores ao meio (Ex.: ordem 7, int(ordemDaMatriz / 2) = 3, meio 4)
        for i in range(int(ordemDaMatriz / 2)):
            matrizTemp.append(['3'] * ordemDaMatriz)  # Linhas preenchidas com 3, quantidade ditada por ordem da matriz
        coluna = 0  # Coluna (índice) con o qual se está trabalhando
        linha = 0  # Linha com a qual se está trabalhando
        for i in range(int(ordemDaMatriz / 2)):
            matrizTemp[linha][coluna] = '1'
            matrizTemp[linha][ordemDaMatriz - (coluna + 1)] = '2'
            linha += 1
            coluna += 1
        if ordemDaMatriz % 2 != 0:  # Se impar, gera linha do meio
            matrizTemp.append(['3'] * ordemDaMatriz)  # Linhas preenchidas com 3, quantidade ditada por ordem da matriz
            # int(ordemDaMatriz / 2) é o meio pq o índice das lista começa em 0, caso contrário seria necessário + 1
            matrizTemp[int(ordemDaMatriz / 2)][int(ordemDaMatriz / 2)] = '2'  # Substitui o meio por 2
        linha -= 1  # linha está 1 acima do desejado (fora de alcance em ordem par e linha do meio em impares), remove 1
        for t in range(int(ordemDaMatriz / 2)):
            matrizTemp.append(matrizTemp[linha][::-1])  # Adiciona à matriz o inverso da linha
            linha -= 1
        for u in matrizTemp:
            u = "".join(u)  # Une os elementos de cada lista em uma só string dentro de uma lista
            matriz.append(u)  # Põe essa lista na matriz final
        for t in matriz:
            print(t)
    except EOFError:  # Encerra em EOF
        break
