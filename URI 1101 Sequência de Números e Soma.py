m, n = map(int, input().split())
while m > 0 and n > 0:  # Programa encerra se um dos valores for 0
    # Seis linhas subsequentes definem maior e menor valores entre m e n
    if m > n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m
    lista = []
    pisoIntervalo = menor
    while len(lista) < (maior - menor) + 1:  # Loop fica computando valores de [menor,maior] até todos estarem na lista
        lista.append(pisoIntervalo)
        pisoIntervalo += 1
    print(*lista, f'Sum={sum(lista)}')
    m, n = map(int, input().split())
