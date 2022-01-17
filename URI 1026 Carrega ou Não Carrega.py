while True:
    try:
        a, b = map(int, input().split())
        # Binário tem 0b no começo pra identificação, tornando em string e reduzindo com [2:] remove-se essa notação
        # e mantém se apenas o valor
        a = str(bin(a))[2:]
        b = str(bin(b))[2:]
        # Condicionais adicionam 0 à esquerda para que não encerre por não haver valor para índice no menor dos valores
        if len(a) > len(b):
            correcao = '0' * (len(a) - len(b))
            b = (correcao + b)
        elif len(a) < len(b):
            correcao = '0' * (len(b) - len(a))
            a = (correcao + a)
        resultadoBin = ''
        indice = 0
        for i in a:
            soma = int(a[indice]) + int(b[indice])  # Soma dos valores de cada unidade de cada variável
            # Binário nunca passa de 1 em uma determinada casa
            if soma > 1:
                resultadoBin = resultadoBin + '0'
            else:
                resultadoBin = resultadoBin + str(soma)
            indice += 1
        resultado = int(resultadoBin, 2)  # Converte de binário para decimal
        print(resultado)
    except EOFError:  # Encerra em EOF
        break
