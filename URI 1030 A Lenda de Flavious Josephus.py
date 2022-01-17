qtdCasos = int(input())
for i in range(qtdCasos):
    numPessoas, tamSaltos = map(int, input().split())
    mortos = []
    soldados = []
    for t in range(numPessoas + 1):
        if t != 0:
            soldados.append(t)
    indiceRemover = tamSaltos + tamSaltos - 1
    soldados.remove(tamSaltos)
    while len(soldados) != 1:
        print(soldados)
        print(indiceRemover)
        soldados.remove(soldados[indiceRemover])
        

    print(soldados)