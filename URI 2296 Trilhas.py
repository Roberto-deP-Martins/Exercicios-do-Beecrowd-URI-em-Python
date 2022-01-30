num_trilhas = int(input())
trilhas = []
for i in range(num_trilhas):
    dados_trilha = input().split()
    dados_trilha = [int(x) for x in dados_trilha]
    trilhas.append(dados_trilha[1:])
for t in trilhas:
    proximo_indice = 1
    dificuldade = 0
    dificuldade_contraria = 0
    testes = 0
    id_trilha = 0
    while testes < 2:
        print(testes)
        if testes == 0:
            direcao = 1
            proximo_indice = 1
        else:
            direcao = -1
            proximo_indice = len(t) - 1
        print(testes, 'for')
        for y in t[:len(t) - 1:direcao]:
            print(testes, 'dentro')
            if testes == 0:
                if y < t[proximo_indice]:
                    print(y, t[proximo_indice])
                    dificuldade += t[proximo_indice] - y
                proximo_indice += 1
            elif testes == 1:
                print(t[:len(t) - 1:direcao])
                if y < t[proximo_indice]:
                    print(f'{dificuldade_contraria} + {t[proximo_indice]} - {y}')
                    dificuldade_contraria += t[proximo_indice] - y
                proximo_indice -= 1
        testes += 1
    if dificuldade_contraria < dificuldade:
        dificuldade = dificuldade_contraria
    trilhas[trilhas.index(t)].append(dificuldade)
    id_trilha += 1
