ultimaRegiao = 13
numRegioes = int(input())
while numRegioes != 0:
    numPularCasas = 1
    achou = False  # Se torna true quando chegar em um valor de pulo em que 13 é o último valor restante
    while not achou:  # Enquanto achou não for True
        regioes = []  # Lista com regiões de 1 a numRegioes
        # Preenche a lista com regiões de 1 a numRegioes
        for i in range(numRegioes):
            regioes.append(i + 1)
        indice = 0  # índice na lista
        # Se torna True quando ultimaRegiao é retirado da lista antes de só sobrar uma região na mesma
        regiaoRetirada = False
        # Roda enquanto a lista de regiões tiver mais de 1 item e ultimaRegiao está na lista
        while len(regioes) > 1 and ultimaRegiao in regioes:
            regioes.pop(indice)  # Remove a região do índice da lista
            # Usa aritmética modular para determinar o próximo índice:
            # Soma os índice com o pulo, subtrai 1 para compensar pelo item removido e, por último, determina o resto
            # dessa operação em uma divisão com o tamanho da lista (operação módulo)
            # Esse tipo de operação é útil para dar "voltas em lista"
            indice = (indice + numPularCasas - 1) % len(regioes)
        if len(regioes) == 1 and regioes[0] == ultimaRegiao:  # Se o último valor remanescente for ultimaRegião
            print(numPularCasas)  # Mostra o número de casas que se deve pular para que isso aconteça
            achou = True
        numPularCasas += 1
    numRegioes = int(input())
