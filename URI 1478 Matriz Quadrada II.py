ordemDaMatriz = int(input())
while ordemDaMatriz != 0:  # Encerra quando usuário digitar 0
    matriz = []
    # Lista que contém a informação se já se alcançou 1 em alguma das colunas, importante pois lista inverte
    # após esse valor.
    chegouMinimo = []
    linhaTemp = []  # Linha temporária para formação da matriz
    primeriaLinha = []
    for i in range(ordemDaMatriz):
        linhaTemp.append('0'.rjust(3))  # Faz linhas compostas pelo número de zeros igual ao num de ordem da matriz
        chegouMinimo.append(False)  # Preenche essa lista com False
        matriz.append(linhaTemp)  # Põe linhaTemp 'ordem da matriz' vezes na matriz
    for val in range(1, ordemDaMatriz + 1):  # Cria a primeira linha, uma contagem de 1 ao valor de ordem da matriz
        primeriaLinha.append(str(val).rjust(3))
    ultimaLinha = sorted(primeriaLinha, reverse=True)  # A última linha será sempre o contrário da primeira
    matriz[0] = primeriaLinha  # Substitui a primeira linha da matriz por primeiraLinha
    matriz[-1] = ultimaLinha  # Substitui a primeira linha da matriz por ultimaLinha
    # Linha é a linha em que se está trabalhando
    for linha in range(ordemDaMatriz - 1):  # Repete uma vez a menos que o número de linhas e colunas
        linhaTemp = []
        indice = 0  # Indice da linha na qual se está trabalhando
        for i in range(ordemDaMatriz):  # Repete o mesmo número do comprimento de cada linha
            # O menor valor é 1, logo ele não pode ser subtraído, apenas somado. Além disso, ele só aparecerá uma vez
            # na primeira linha, e a partir daí só sofrerá somas.
            if int(primeriaLinha[indice]) == 1:
                # Valor da mesma coluna da linha anterior + 1
                linhaTemp.append(str(int(matriz[linha][indice]) + 1).rjust(3))
                indice += 1
            else:
                # A partir do momento que uma coluna tem o valor 1, o seu valor deve passar a apenas aumentar
                if chegouMinimo[indice]:
                    # Valor da mesma coluna da linha anterior + 1
                    linhaTemp.append(str(int(matriz[linha][indice]) + 1).rjust(3))
                else:  # Se a coluna ainda não tiver o valor 1
                    # Valor da mesma coluna da linha anterior - 1
                    linhaTemp.append(str(int(matriz[linha][indice]) - 1).rjust(3))
                # Se na linha anterior o valor na coluna é 2, então na linha atual é 1, e isso é reportado na lista
                # com a mudança de 'Não' para 'Sim' no indice da lista de verificação igual à coluna em que ocorreu
                if int(matriz[linha][indice]) == 2:
                    chegouMinimo[indice] = True
                indice += 1
            matriz[linha + 1] = linhaTemp  # Adiciona a linha gerada à matriz
    for t in matriz:
        print(*t)
    print()
    ordemDaMatriz = int(input())
