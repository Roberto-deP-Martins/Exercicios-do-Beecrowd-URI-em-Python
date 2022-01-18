def desmembraMomento(e):  # Pega hora, minuto e segundo da string
    hora = int(e[0:2])
    minuto = int(e[5:8])
    segundo = int(e[10:])
    return hora, minuto, segundo


def obterDia(e):  # Pega dia na string
    dia = int(e[4:])
    return dia


def conversaoSegundos(h, m, s):  # Converte o horário dado para segundos (horas e minutos para segundos seguido de soma)
    segundos = (h * 3600) + (m * 60) + s  # 3600 = 60² (Transforma hora direto para segundo)
    return segundos


def converter(e):  # Converte o tempo total do evento, em segundos, para horas, dias, minutos e segundos
    dias = e // 86400  # 86400 = 60 (converte aos minutos) * 60 (converte às horas) * 24 (converte aos dias)
    horas = (e % 86400) // 3600  # O resto da divisão é os segundos "sobrando", dividir por 3600 transforma em horas
    segundos = (e % 86400) % 3600  # O resto das horas (e % 86400), são os segundos sobrando
    if segundos >= 60:  # Se tiver mais que 60 segundos, isso é pelo menos um minuto, e precisa ser convertido
        minutos = segundos // 60  # Conversão segundos para minutos
        segundos = segundos % 60  # O resto é os segundos que sobram
    else:
        minutos = 0  # Caso não haja mais que 60 segundos, haverão 0 mminutos
    return dias, horas, minutos, segundos


diaInicio = obterDia(input())
momentoInicio = input()
horaInicio, minutoInicio, segundoInicio = desmembraMomento(momentoInicio)
diaFinal = obterDia(input())
momentoFinal = input()
horaFinal, minutoFinal, segundoFinal = desmembraMomento(momentoFinal)
momentoInicio = conversaoSegundos(horaInicio, minutoInicio, segundoInicio)
momentoFinal = conversaoSegundos(horaFinal, minutoFinal, segundoFinal)
if momentoFinal != momentoInicio:  # Caso fosse igual só seria necessário obter a diferença de dias
    qtdDias = diaFinal - diaInicio
    qtdDiasSegundos = qtdDias * 86400  # 86400 = 60² (horas pra segundos) * 24 (dias pra horas)
    momentoFinal = qtdDiasSegundos + momentoFinal
    tempoDoEvento = momentoFinal - momentoInicio
    diasEvento, horasEvento, minutosEvento, segundosEvento = converter(tempoDoEvento)
    print(diasEvento, 'dia(s)')
    print(horasEvento, 'hora(s)')
    print(minutosEvento, 'minuto(s)')
    print(segundosEvento, 'segundo(s)')
else:
    qtdDias = diaFinal - diaInicio
    print(qtdDias, 'dias(s)')
    print(0, 'hora(s)')
    print(0, 'minuto(s)')
    print(0, 'segundo(s)')