distancia_total = 0
for i in range(int(input())):
    intervalo_horas, velocidade_intervalo = map(int, input().split())
    distancia_total += intervalo_horas * velocidade_intervalo
print(distancia_total)