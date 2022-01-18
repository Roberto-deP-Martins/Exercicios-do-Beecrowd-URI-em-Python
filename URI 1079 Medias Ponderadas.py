qtdCasos = int(input())
for i in range(qtdCasos):
    a, b, c = map(float, input().split())
    media = ((2 * a) + (b * 3) + (c * 5)) / (2 + 3 + 5)
    print('%.1f' % media)
