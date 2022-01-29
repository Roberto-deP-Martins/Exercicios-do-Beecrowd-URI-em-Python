def encontra_menor(vetor):
    vetor_organizado = sorted(vetor)
    menor = vetor_organizado[0]
    return menor, vetor.index(menor)


tamanho_lista = int(input())
lista = []
valores_lista = map(int, input().split())
lista.extend(valores_lista)
menor_valor, posicao = encontra_menor(lista)
print('Menor valor:', menor_valor)
print('Posicao:', posicao)
