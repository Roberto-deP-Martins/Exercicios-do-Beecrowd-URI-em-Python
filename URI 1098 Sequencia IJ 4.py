i = 0
j = 0
t = 0
valores = [0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6, 1.8, 2, 2.2]
repeticoes = 0
while repeticoes != 11:
    while j != (t + 3):
        j += 1
        if repeticoes == 5 or repeticoes == 10:  # Nesses casos i é 1 ou 2, deve-se arrendondar para não ser 1.0 e 2.0
            print(f'I={round(i)} J={j}')
        else:
            print(f'I={round(i, 1)} J={j}')  # Arredonda-se para evitar erros de cálculo e ficar igual à saída esperada
    repeticoes += 1
    i += 0.2
    # Linhas subsequentes determinam valores presentes na lista para variáveis de acordo com a etapa em que o
    # programa está ( o valor repeticoes aumentar faz j e t assumirem valores de posições diferentes da lista
    j = valores[repeticoes - 1]
    t = valores[repeticoes - 1]
