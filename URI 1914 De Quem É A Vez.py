qtdTestes = int(input())  # Número de vezes que o programa vai rodar
for i in range(qtdTestes):
    jogador1 = []  # Lista com informações pertinentes ao Jogador 1, esvazia à cada loop
    jogador2 = []  # Lista com informações pertinentes ao Jogador 2, esvazia à cada loop
    entrada = input().split()
    # Os dois primeiros itens da entrada são referentes ao Jogador 1, os dois seguintes, ao Jogador 2.
    jogador1.append(entrada[0])
    jogador1.append(entrada[1])
    jogador2.append(entrada[2])
    jogador2.append(entrada[3])
    parcela1, parcela2 = map(int, input().split())  # Valores à serem somados
    totalSoma = parcela1 + parcela2
    if totalSoma % 2 == 0:  # Se for par
        if 'PAR' in jogador1:  # Se o Jogador 1 tiver escolhido Par, ele vence
            print(jogador1[0])
        else:   # Se o Jogador 1 tiver escolhido Par e o número não for par, Jogador 2 vence
            print(jogador2[0])
    else:  # Se for ímpar
        if 'IMPAR' in jogador1:  # Se o Jogador 1 tiver escolhido Ímpar, ele vence
            print(jogador1[0])
        else:  # Se o Jogador 1 tiver escolhido Ímpar e o número não for par, Jogador 2 vence
            print(jogador2[0])
