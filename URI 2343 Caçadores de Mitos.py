matriz = []
for i in range(501):
    matriz.append([0] * 501)
qtdTestes = int(input())
repetiu = False
for i in range(qtdTestes):
    x, y = map(int,input().split())
    if matriz[y][x] == 0:
        matriz[y][x] += 1
    else:
        print(1)
        repetiu = True
        break
if not repetiu:
    print('0')

# Tuplas
