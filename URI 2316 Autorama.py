qtd_postos, qtd_carrinhos, qtd_leituras = map(int, input().split())
dados = []
entradas = []
for i in range(qtd_carrinhos):  # Adiciona dicionários para os carrinhos
    dados.append({'numero' : i + 1, 'voltas' : 0, 'posto' : 0, 'acumulado' : 0})
for i in range(qtd_leituras):
    entrada = tuple(input().split())
    numero_carro = int(entrada[0])

    # garante que ficarão apenas os últimos movimentos dos carros na lista para ordenação
    if numero_carro in entradas:
        entradas.remove(numero_carro)
    entradas.append(numero_carro)

    
    id_carro, posto = map(int, entrada)
    id_carro -= 1
    if dados[id_carro]['posto'] == posto - 1:
        dados[id_carro]['posto'] += 1
        dados[id_carro]['acumulado'] += 1
        if dados[id_carro]['posto'] == qtd_postos:
            dados[id_carro]['voltas'] += 1
            dados[id_carro]['acumulado'] += 1
            dados[id_carro]['posto'] = 0
dados = sorted(dados, key=lambda d: d['acumulado'], reverse=True)  # Organiza por acumulado (postos + voltas)
empates = []  # Lista de carros com mesmo núm acumulado
valor_atual = dados[0]['acumulado']
empates_num_acumulado = []  # Lista com elementos com mesmo acumulado
for item in dados:
    if item['acumulado'] == valor_atual:
        item['idx'] = entradas.index(item['numero'])
        empates_num_acumulado.append(item)
    else:
        empates.append(empates_num_acumulado)
        valor_atual = item['acumulado']
        item['idx'] = entradas.index(item['numero'])
        empates_num_acumulado = []
        empates_num_acumulado.append(item)
empates.append(empates_num_acumulado)
for i in empates:
    empates[empates.index(i)] = sorted(i, key=lambda d: d['idx'])  # Organiza cada tipo de empate por ordem de entrada de posição
for i in empates:
    for t in i:
        if t == empates[-1][-1]:
            print(t['numero'])
        else:
            print(t['numero'], end=' ')