def trata_resultado(vetor):
    vetor.remove('x')
    vetor = [int(x) for x in vetor]
    return vetor


def atribui_pontos(gols_time1, gols_time2, pontuacao_time1, pontuacao_time2):
    if gols_time1 > gols_time2:
        pontuacao_time1 += 3
    elif score_time1 < score_time2:
        pontuacao_time2 += 3
    else:
        pontuacao_time1 += 1
        pontuacao_time2 += 1
    return pontuacao_time1, pontuacao_time2


for i in range(int(input())):
    total_time1, total_time2 = 0, 0
    score_time1, score_time2 = 0, 0
    for t in range(2):
        resultado_partida = trata_resultado(input().split())
        if t == 0:  # Primeira rodada
            score_time1 = resultado_partida[0]
            acumulado_time1 = score_time1
            score_time2 = resultado_partida[1]
            acumulado_time2 = score_time2
            score_time2_visitante = score_time2
            total_time1, total_time2 = atribui_pontos(score_time1, score_time2, total_time1, total_time2)

        else:  # Segunda rodada
            score_time1 = resultado_partida[1]
            acumulado_time1 += score_time1
            score_time1_visitante = resultado_partida[1]
            score_time2 = resultado_partida[0]
            acumulado_time2 += score_time2
            total_time1, total_time2 = atribui_pontos(score_time1, score_time2, total_time1, total_time2)
            if total_time1 == total_time2:
                if (acumulado_time1 - acumulado_time2) > (acumulado_time2 - acumulado_time1):
                    print('Time 1')
                elif (acumulado_time1 - acumulado_time2) < (acumulado_time2 - acumulado_time1):
                    print('Time 2')
                else:
                    if score_time1_visitante > score_time2_visitante:
                        print('Time 1')
                    elif score_time2_visitante > score_time1_visitante:
                        print('Time 2')
                    else:
                        print('Penaltis')
            elif total_time1 < total_time2:
                print('Time 2')
            else:
                print('Time 1')
