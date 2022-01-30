ordemDaMatriz = int(input())
while ordemDaMatriz != 0:  # Encerra quando usuário digitar 0
    numeroInicio = 1  # Primeiro da primeira linha
    matrizInt = []  # Matriz com os valores como int para ser convertida para str depois
    linhaTemp = []  # Linhas temporárias para a construção da matriz
    # Gera a primeira linha
    for i in range(ordemDaMatriz):  # Num de ocorrências determinado pela ordem da matriz
        linhaTemp.append(numeroInicio)
        numeroInicio = numeroInicio * 2  # Vai fazendo as multiplicações por 2 e adicionando à lista
    matrizInt.append(linhaTemp)  # Adiciona primeira linha à matriz
    coluna = 1  # Coluna na qual se está trabalhando, começa em 1 pois a primeira linha já foi gerada
    # Gera linhas seguintes
    for i in range(ordemDaMatriz - 1):  # Num de ocorrências determinado pela ordem da matriz, pois 1ª linha já existe
        linhaTemp = []
        num = matrizInt[0][coluna]  # Num base que será multiplicado corresponde ao num da 1ª linha na posição da coluna
        for t in range(ordemDaMatriz):
            if len(linhaTemp) == 0:  # Primeiro valor adicionado à linha
                linhaTemp.append(matrizInt[0][coluna])
                num *= 2
            else:
                linhaTemp.append(num)
                num *= 2
        coluna += 1
        matrizInt.append(linhaTemp)  # Adiciona linha à matriz
    matrizFinal = []  # Matriz com strings formatadas
    # O número de unidades do justificado é dado pelo tamanho do maior item, que sempre será o último
    tamanhoJustificado = len(str(matrizInt[-1][-1]))
    for t in matrizInt:
        linhaFinal = []
        for i in t:
            # Põe na linha a str formatada do item da lista original
            linhaFinal.append(str(i).rjust(tamanhoJustificado))
        matrizFinal.append(linhaFinal)  # Põe a linha na matriz nova
    for t in matrizFinal:
        print(*t)
    print()
    ordemDaMatriz = int(input())
