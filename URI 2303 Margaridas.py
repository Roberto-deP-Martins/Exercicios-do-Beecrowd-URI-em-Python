matriz_plantacao = []
qtd_linhas_plantacao, qtd_colunas_plantacao, qtd_linhas_lote, qtd_colunas_lote = map(int, input().split())
for i in range(qtd_linhas_plantacao):
    matriz_plantacao.append(list(map(int, input().split())))
maior_total = -1
total = 0
for i in range(0, qtd_linhas_plantacao, qtd_linhas_lote):
    for j in range(0, qtd_colunas_plantacao, qtd_colunas_lote):
        for k in range(i, i + qtd_linhas_lote):
            for l in range(j, j + qtd_colunas_lote):
                total += matriz_plantacao[k][l]
        if total > maior_total:
            maior_total = total
        total = 0
print(maior_total)