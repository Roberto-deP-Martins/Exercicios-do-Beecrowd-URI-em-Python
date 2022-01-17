inicio, fim = map(int, input().split())
if fim < inicio:
    # Adicionar as 24 horas do dia anterior quando o
    # jogo termina no dia seguinte permite o cálculo correto
    fim += 24
    tempo = fim - inicio
    print('O JOGO DUROU {} HORA(S)'.format(tempo))
elif fim == inicio:
    # Se o tempo do inicio e fim são iguais se passaram 24
    # horas com o jogo terminando no mesmo horário do dia seguinte
    print('O JOGO DUROU 24 HORA(S)')
else:
    tempo = fim - inicio
    print('O JOGO DUROU {} HORA(S)'.format(tempo))
