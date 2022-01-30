def binario():
    for i in entradas:
        simbolos = []  # Símbolos de cada entrada (- ou *)
        for t in i:
            simbolos.append(t)
        indice = 0  # Índice que está se analisando
        if '*' in simbolos:
            for u in simbolos:
                if u == '*':
                    # Expoente da potência pra calcular binário, subtrai o índice de 2 pq calcula binário na ordem
                    # oposta à leitura da lista
                    expoente = 2 - indice
                    binarios.append(2 ** expoente)
                    indice += 1
                else:
                    indice += 1
    return sum(binarios)


qtdNumeros = 0  # Quantidade de números já obtidos (máx 3)
while qtdNumeros < 3:
    binarios = []  # Lista de binários obtidos
    entradas = []
    entrada = input()
    while entrada != 'caw caw':  # Obtém os cálculos e reseta a lista quando digitarem caw caw
        entradas.append(entrada)
        entrada = input()
    numSorteado = binario()
    print(numSorteado)
    qtdNumeros += 1
