def organiza_palavras(string):
    palavras = string.split()
    tamanhos = [len(palavra) for palavra in palavras]
    ordenado = ''
    while palavras:
        idx = tamanhos.index(max(tamanhos))  # Índice do 1.º dos itens de maior tamanho, 2.º, 3.º e assim por diante
        ordenado = ordenado + palavras[idx] + ' '

        # Remove o tamanho e palavra que acabou de ser adicionada a string ordenada
        tamanhos.pop(idx)
        palavras.pop(idx)

    ordenado = ordenado.rstrip()  # Remove o espaço em branco à direita da string
    return ordenado


qtd_casos = int(input())
for i in range(qtd_casos):
    frase = input()
    frase_organizada = organiza_palavras(frase)
    print(frase_organizada)
