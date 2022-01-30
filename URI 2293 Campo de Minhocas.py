qtd_linhas, qtd_colunas = map(int, input().split())
matriz = []
qtd_minhocas_unidades = []

for linha in range(qtd_linhas):
    linha_formatada = list(map(int, input().split()))
    qtd_minhocas_unidades.append(sum(linha_formatada))
    matriz.append(linha_formatada)
for coluna in range(qtd_colunas):
    qtd_minhocas = 0
    for linna in range(qtd_linhas):
        qtd_minhocas += matriz[linna][coluna]
    qtd_minhocas_unidades.append(qtd_minhocas)
print(max(qtd_minhocas_unidades))