metros_pretendidos, comprimento_pista = map(int, input().split())
# Resto dá o ponto de término pois dá a distância que sobra após voltas completas
print(metros_pretendidos % comprimento_pista)
