for i in range(int(input())):
    listaFibonacci = [0, 1]  # A lista sempre começa com 0 e 1
    # QtdNumeros determina quantos itens estarão na lista, remove-se 1 para existir índice 4 na lista
    qtdNumeros = int(input()) - 1
    indice = 1  # Começa no segundo (1) pois já há dois na lista
    for t in range(qtdNumeros):  # Enquanto a lista não tiver a quantidade de números digitadas loop continua
        listaFibonacci.append((listaFibonacci[indice - 1] + listaFibonacci[indice]))  # Faz soma dos 2 prévios na lista
        indice += 1  # Avança o índice na lista ao qual a linha anterior vai se referir
    print(f'Fib({qtdNumeros + 1}) = {listaFibonacci[qtdNumeros + 1]}')  # Printa o indice digitado e o valor no indice
