numRodadas = int(input())
while numRodadas != 0:
    pontuacaoA = 0
    pontuacaoB = 0
    for i in range(numRodadas):
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a > b:
            pontuacaoA += 1
        elif b > a:
            pontuacaoB += 1
    print(pontuacaoA, pontuacaoB)
    numRodadas = int(input())
