def variacao(temperaturaUm, temperaturaDois):
    variacao = temperaturaDois - temperaturaUm  # O delta da temperatura
    return variacao


feliz = ':)'
triste = ':('
diaUm, diaDois, diaTres = map(int, input().split())  # Separa os valores nas três variáveis
variacaoUmDois = variacao(diaUm, diaDois)
variacaoDoisTres = variacao(diaDois, diaTres)
if variacaoUmDois < 0 <= variacaoDoisTres:  # Temperatura diminui do dia 1 pra 2 e é igual ou maior ao 2 no dia 3
    print(feliz)
elif variacaoUmDois > 0 >= variacaoDoisTres:  # Temp aumenta do dia 1 pra 2 e do dia 2 pro 3 foi constante ou diminuiu
    print(triste)
elif variacaoUmDois > 0 and variacaoDoisTres > 0:  # Temp aumenta do dia 1 pro 2 e do dia 2 pro 3
    if variacaoDoisTres < variacaoUmDois:  # Temp aumentou menos do dia 2 pra 3 do que de 1 pra 2
        print(triste)
    elif variacaoDoisTres >= variacaoUmDois:  # Variação da temp de 2 pra 3 foi a mesma ou maior que de 1 pra 2
        print(feliz)
elif variacaoUmDois < 0 and variacaoDoisTres < 0:  # Temperatura diminuiu de 1 pra 2 e de 2 pra 3
    if variacaoDoisTres > variacaoUmDois:  # Variação da temp de 2 pra 3 foi maior que de 1 pra 2
        print(feliz)
    elif variacaoDoisTres <= variacaoUmDois:  # Variação de dois pra três foi menor ou igual de 1 pra 2
        print(triste)
elif variacaoUmDois == 0:  # Temperatura de 1 pra 2 se manteve constante
    if variacaoDoisTres > 0:  # De 2 pra 3 aumentou
        print(feliz)
    else:  # De 2 pra 3 diminuiu
        print(triste)
