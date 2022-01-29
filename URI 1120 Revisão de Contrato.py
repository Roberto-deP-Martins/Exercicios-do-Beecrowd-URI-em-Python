digitoFalho, numNegociado = input().split()
while (digitoFalho and numNegociado) != '0':  # Encerra quando o usuário digitar '0 0'
    if digitoFalho in numNegociado:  # Se o dígito defeituoso estiver no número digitado
        numNegociado = list(numNegociado)  # Transforma a string do número em uma lista, onde os dígitos ficam separados
        while digitoFalho in numNegociado:  # Enquanto existir ocorrência dele, ele será removido da lista
            numNegociado.remove(digitoFalho)
        numNegociado = ''.join(numNegociado)  # Une os dígitos da lista em uma string novamente
        if numNegociado == '':  # Se não tiver sobrado nada após a remoção, dá o valor zero
            print(0)
        else:
            print(int(numNegociado))  # Caso contrário dá print no número sem os dígitos falhos
    else:  # Caso o dígito falho não esteja presente, só dá print no número digitado
        print(numNegociado)
    digitoFalho, numNegociado = input().split()