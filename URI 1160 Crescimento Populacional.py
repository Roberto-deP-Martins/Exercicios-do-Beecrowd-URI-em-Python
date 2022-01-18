qtdTestes = int(input())
for i in range(qtdTestes):  # Repete o número de vezes digitado
    populacaoA, populacaoB, crescimentoA, crescimentoB = map(float, input().split())  # crescimentos são porcentagem
    # Próximas duas linhas transformam em porcentagem e adicionam 1 por ser crescimento (+1% vira 1.01, +10% = 1.10,etc)
    crescimentoA = 1 + crescimentoA / 100
    crescimentoB = 1 + crescimentoB / 100
    populacaoA = int(populacaoA)
    populacaoB = int(populacaoB)
    multiplicadorBase = 1
    anos = 0
    while populacaoA <= populacaoB:  # Termina quando população de A for maior que B
        if crescimentoB == 0:  # Caso cidade B não tenha crescimento
            populacaoA *= crescimentoA
            populacaoA = int(populacaoA)  # Int é uma forma de se arredondar para baixo até .9999999999999999 (16 noves)
            anos += 1
            if anos > 100:
                break  # Encerra o loop após 100 anos, pois a resposta simplesmente dirá ser mais de 1 século
        else:  # Caso contrário
            anos += 1
            populacaoA *= crescimentoA
            populacaoA = int(populacaoA)
            populacaoB *= crescimentoB
            populacaoB = int(populacaoB)
            if anos > 100:
                break
    if anos > 100:
        print('Mais de 1 seculo.')
    else:
        print(f'{anos} anos.')
