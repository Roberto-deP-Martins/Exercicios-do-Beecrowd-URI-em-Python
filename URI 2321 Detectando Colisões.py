x0_retangulo1, y0_retangulo1, x1_retangulo1, y1_retangulo1 = map(int, input().split())
x0_retangulo2, y0_retangulo2, x1_retangulo2, y1_retangulo2 = map(int, input().split())
intersectou = False
# Verifica se algum ponto da aresta horizontal inferior do retângulo 1 intersecta
coordenada = [x0_retangulo1, y0_retangulo1]
for i in range(x0_retangulo1, x1_retangulo1 + 1):
    if x0_retangulo2 <= coordenada[0] <= x1_retangulo2 and y0_retangulo2 <= coordenada[1] <= y1_retangulo2:
        print(1)
        intersectou = True
        break
    else:
        coordenada[0] += 1
if not intersectou:
    # Verifica se algum ponto da aresta horizontal superior do retângulo 1 intersecta
    coordenada = [x0_retangulo1, y1_retangulo1]
    for i in range(x0_retangulo1, x1_retangulo1 + 1):
        if x0_retangulo2 <= coordenada[0] <= x1_retangulo2 and y0_retangulo2 <= coordenada[1] <= y1_retangulo2:
            print(1)
            intersectou = True
            break
        else:
            coordenada[0] += 1
# Verifica se algum ponto da aresta horizontal inferior do retângulo 2 intersecta
if not intersectou:
    coordenada = [x0_retangulo2, y0_retangulo2]
    for i in range(x0_retangulo2, x1_retangulo2 + 1):
        if x0_retangulo1 <= coordenada[0] <= x1_retangulo1 and y0_retangulo1 <= coordenada[1] <= y1_retangulo1:
            print(1)
            intersectou = True
            break
        else:
            coordenada[0] += 1
# Verifica se algum ponto da aresta horizontal superior do retângulo 2 intersecta
if not intersectou:
    coordenada = [x0_retangulo2, y1_retangulo2]
    for i in range(x0_retangulo2, x1_retangulo2 + 1):
        if x0_retangulo1 <= coordenada[0] <= x1_retangulo1 and y0_retangulo1 <= coordenada[1] <= y1_retangulo1:
            print(1)
            intersectou = True
            break
        else:
            coordenada[0] += 1
if not intersectou:
    print(0)
