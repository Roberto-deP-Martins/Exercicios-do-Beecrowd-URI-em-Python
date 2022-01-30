numPartidas = int(input())
n = 0  # Variável que guarda o número do teste que está ocorrendo
while numPartidas != 0:  # Encerra quando o usuário digitar 0
    n = n + 1  # Adiciona um ao número do teste e dita quantas rodadas ocorrerão
    print("Teste", n)
    jogador1 = input()  # Nome jogador 1
    jogador2 = input()  # Nome jogador 2
    for i in range(numPartidas):
        # Duas variáveis que dizem o número de dedos que cada jogador mostrou
        dedosJogador1, dedosJogador2 = map(int, input().split())
        # Primeiro jogador sempre escolhe par, segundo sempre ímpar
        if (dedosJogador1 + dedosJogador2) % 2 == 0:  # Se par
            print(jogador1)
        else:  # Se ímpar
            print(jogador2)
    print()
    numPartidas = int(input())
