xP1, yP1 = map(float, input().split())
xP2, yP2 = map(float, input().split())
distancia = ((xP2 - xP1) ** 2 + (yP2 - yP1) ** 2) ** (1/2)
print(f'{distancia:.4f}')