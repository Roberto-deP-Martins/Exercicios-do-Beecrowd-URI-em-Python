qtd_secoes = int(input())
lista_territorios = list(map(int, input().split()))
ponto_divisao = (qtd_secoes // 2) + 1
achou_divisao = False
while not achou_divisao:
    total_primeira_metade = sum(lista_territorios[0:ponto_divisao])
    total_segunda_metade = sum(lista_territorios[ponto_divisao:])

    # Remover
    print(lista_territorios[0:ponto_divisao])
    print(lista_territorios[ponto_divisao:])
    print(total_primeira_metade)
    print(total_segunda_metade)


    if total_primeira_metade == total_segunda_metade:
        print(ponto_divisao)
        achou_divisao = True
    elif total_primeira_metade < total_segunda_metade:
        ponto_divisao += 1
    else:
        ponto_divisao -= 1
