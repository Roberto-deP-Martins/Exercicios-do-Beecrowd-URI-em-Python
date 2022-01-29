x = 1
vitoriasGremio,vitoriasInter, empates, grenais = 0, 0, 0, 0
while x == 1:
    golsInter, golsGremio = map(int, input().split())
    grenais = grenais + 1
    if golsGremio > golsInter:
        vitoriasGremio = vitoriasGremio + 1
    elif golsInter > golsGremio:
        vitoriasInter = vitoriasInter + 1
    else:
        empates = empates + 1
    pergunta = int(input("Novo grenal (1-sim 2-nao)\n", ))
    if pergunta == 2:
        x = x - 1
if vitoriasInter > vitoriasGremio:
    print(grenais,"grenais")
    print("Inter:",vitoriasInter, sep='')
    print("Gremio:",vitoriasGremio, sep='')
    print("Empates:",empates, sep='')
    print("Inter venceu mais")
elif vitoriasInter < vitoriasGremio:
    print(grenais, "grenais")
    print("Inter:",vitoriasInter, sep='')
    print("Gremio:",vitoriasGremio, sep='')
    print("Empates:",empates, sep='')
    print("Inter venceu mais")
elif vitoriasInter == vitoriasGremio:
    print(grenais, "grenais")
    print("Inter:",vitoriasInter, sep='')
    print("Gremio:",vitoriasGremio, sep='')
    print("Empates:",empates, sep='')
    print("Nao houve vencdedor")