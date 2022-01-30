def trata_cartas(lista):
    # A ordem de valor simbólico das cartas "4 5 6 7 Q J K A 2 3", foi reescrita como uma sequência de 1 a 10, 
    # sendo 4 = 1, 5 = 2, 6 = 3, 7 = 4, Q = 5...
    # O dicionário tem o valor com o qual cada digito da lista corresponde na nova escala de 1 a 10
    traducao = {1 : 8, 2 : 9, 3 : 10, 4 : 1, 5 : 2, 6 : 3, 7 : 4, 11 : 6, 12 : 5, 13 : 7}  # 
    for idx in range(3):
        lista[idx] = traducao[lista[idx]]  # Substitui os valores da lista pelas suas correspondências
    return lista


qtd_testes = int(input())
total_adalberto = 0
total_bernadete = 0
for i in range(qtd_testes):
    pontos_adalberto = 0
    pontos_bernadete = 0
    cartas = [int(x) for x in input().split()]  # Converte todas as string numéricas da lista para ints
    cartas_adalberto = cartas[0:3]
    cartas_adalberto = trata_cartas(cartas_adalberto)
    cartas_bernadete = cartas[3:]
    cartas_bernadete = trata_cartas(cartas_bernadete)
    for i in range(4):
        if pontos_bernadete == 2:
            total_bernadete += 1
            break
        elif pontos_adalberto == 2:
            total_adalberto += 1
            break
        elif cartas_adalberto[i] > cartas_bernadete[i]:
            pontos_adalberto += 1
        elif cartas_adalberto[i] < cartas_bernadete[i]:
            pontos_bernadete += 1
        else:
            pontos_adalberto += 1
print(total_adalberto, total_bernadete)