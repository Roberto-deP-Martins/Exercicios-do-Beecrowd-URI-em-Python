unidadesDias = (365, 30, 1)
unidadesPalavras = ('ano(s)', 'mes(es)', 'dia(s)')
qtdDias = int(input())
for i in unidadesDias:
    unidade = unidadesPalavras[unidadesDias.index(i)]
    if qtdDias // i > 0:
        print(f'{qtdDias // i} {unidade}')
        qtdDias = qtdDias % i
    else:
        print(f'0 {unidade}')
