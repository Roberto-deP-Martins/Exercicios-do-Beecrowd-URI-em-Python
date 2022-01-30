while True:
    matrizTemp = []
    try:
        tamanho = int(input())  # Tamanho da matriz
        for i in range(tamanho):  # Gera o mesmo número de linhas de tamanho
            matrizTemp.append(['0'] * tamanho)  # A linha tem o zero aparecendo o mesmo número de tamanho
        diagonal1 = 0  # Posição da diagonal esquerda
        diagonal2 = tamanho - 1  # Posição da diagonal direita
        linha = 0  # Linha na qual se está trabalhando
        # O quadrado com '1' sempre começa na posição tamanho/3
        for i in range(tamanho // 3):  # Até o início do quadrado
            matrizTemp[linha][diagonal1] = '2'
            matrizTemp[linha][diagonal2] = '3'
            diagonal1 += 1
            diagonal2 -= 1
            linha += 1
        qtdUnicos = linha  # Quantidade de linhas anteriores ao quadrado com '1' e que contém diagonais
        linhaMeio = (tamanho // 2)  # Linha do Meio da Matriz
        indiceMeio = (tamanho // 2)  # Posição do meio da matriz nessa linha
        indiceInicio = diagonal1
        indiceFinal = diagonal2
        for t in range(indiceFinal - indiceInicio + 1):  # Num de elementos entre as diagonais, onde ficará o quadrado
            for i in range(indiceFinal - indiceInicio + 1):
                matrizTemp[linha][indiceInicio] = '1'
                indiceInicio += 1
            indiceInicio = diagonal1
            linha += 1
        matrizTemp[linhaMeio][indiceMeio] = '4'  # Põe o 4 no meio da matriz
        diagonal1 -= 1
        diagonal2 += 1
        linha = tamanho - qtdUnicos  # Primeira linha após quadrado
        for i in range(tamanho // 3):  # Inverso da primeira vez
            matrizTemp[linha][diagonal1] = '3'
            matrizTemp[linha][diagonal2] = '2'
            diagonal1 -= 1
            diagonal2 += 1
            linha += 1
        matrizFinal = []
        for t in matrizTemp:
            t = ''.join(t)  # Junta os elementos em uma só string
            matrizFinal.append(t)  # Põe em uma linha na matriz
        for t in matrizFinal:
            print(t)
        print()
    except EOFError:  # Encerra com erro de EOF
        break
