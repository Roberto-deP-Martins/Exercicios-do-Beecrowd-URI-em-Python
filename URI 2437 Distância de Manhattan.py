# Essa categoria de questão pode ser facilmente resolvida através da forma de geometria chamada geometria pombalina,
# geometria de taxi ou distância de Manhattan, onde a distância é calculada pela soma das diferenças absolutas entre
# os valores x e y

x1, y1, x2, y2 = map(int, input().split())
distancia = abs(x1 - x2) + abs(y1 - y2)
print(distancia)