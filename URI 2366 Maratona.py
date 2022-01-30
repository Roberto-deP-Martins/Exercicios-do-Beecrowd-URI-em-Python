qtd_postos_agua, dist_intermediaria_media = map(int, input().split())
pos_postos = list(map(int, input().split()))
pos_postos.append(42195)
completou = True
for pos in pos_postos[1:]:
    distancia = pos - pos_postos[pos_postos.index(pos) - 1]
    if distancia > dist_intermediaria_media:
        print('N')
        completou = False
        break
if completou:
    print('S')