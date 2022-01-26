def num_coluna(vetor, coluna):  # Pega o número representado pela coluna verticalmente
    num = ''
    for linha in range(4):
        num += vetor[linha][coluna]
    num = int(num)
    return num


def decodifica(f, l, vetor):
    frase = ''
    for coluna in range(1, len(vetor[0]) - 1):
        numero = num_coluna(vetor, coluna)
        letra = chr((f * numero + l) % 257)
        frase += letra
    return frase


matriz = []
for i in range(4):  # 4 linhas
    matriz.append(input())
num_F = num_coluna(matriz, 0)
num_L = num_coluna(matriz, -1)
frase_matring = decodifica(num_F, num_L, matriz)
print(frase_matring)
