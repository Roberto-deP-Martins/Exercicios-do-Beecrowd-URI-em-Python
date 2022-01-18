horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, input().split())
# Próximas duas linhas convertem para minuto para facilitar operações
momentoInicial = (horaInicial * 60) + minutoInicial
momentoFinal = (horaFinal * 60) + minutoFinal
if momentoFinal < momentoInicial:
    # Adicionar as 24 horas do dia anterior quando o
    # jogo termina no dia seguinte permite o cálculo correto
    momentoFinal += (24 * 60)
    tempo = momentoFinal - momentoInicial
    tempoHoras = tempo // 60  # Dá as horas que se passaram
    tempoMinutos = tempo % 60  # Dá os minutos que se passaram
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempoHoras, tempoMinutos))
elif momentoFinal == momentoInicial:
    # Se o momento do inicio e fim são iguais se passaram 24
    # horas com o jogo terminando no mesmo horário do dia seguinte
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    tempo = momentoFinal - momentoInicial
    tempoHoras = tempo // 60  # Dá as horas que se passaram
    tempoMinutos = tempo % 60  # Dá os minutos que se passaram
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(tempoHoras, tempoMinutos))
