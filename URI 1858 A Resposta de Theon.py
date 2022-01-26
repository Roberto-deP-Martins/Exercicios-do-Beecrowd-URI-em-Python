numPessoas = int(input())
pessoas = input().split()  # Separa as pessoas (representadas por números)
pessoas = [int(i) for i in pessoas]  # (Converte pra int os elementos da lista)
pessoasCrescente = sorted(pessoas)  # Lista anterior em ordem crescente
print(pessoas.index(pessoasCrescente[0]) + 1)  # Índice da pessoa com menor número (+1 pra compensar contar a partir 0)
