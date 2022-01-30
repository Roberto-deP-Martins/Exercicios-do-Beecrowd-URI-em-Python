# Zero é preto, um é branco

linhas = int(input())
colunas = int(input())
tabuleiro = []
primeira_linha = []
cor = 1  # O primeiro quadrado do tabuleiro sempre é branco
for coluna in range(colunas):
    primeira_linha.append(cor)
    if cor == 1:  # se o quadrado atual é branco, o próximo é preto
        cor = 0
    else:  # se o quadrado atual é preto, o próximo é branco
        cor = 1
tabuleiro.append(primeira_linha)
# Produz 1 ao menos que o número de linhas do tabuleiro pois primeira linha já foi gerada
for linha in range(linhas - 1):
    linha_em_producao = []
    for coluna in range(colunas):
        if tabuleiro[linha][coluna] == 1:  # se o quadrado acima é branco, o próximo é preto
            linha_em_producao.append(0)
        else:  # se o quadrado acima é preto, o próximo é branco
            linha_em_producao.append(1)
    tabuleiro.append(linha_em_producao)
print(tabuleiro[-1][-1])  # Canto inferior direito
