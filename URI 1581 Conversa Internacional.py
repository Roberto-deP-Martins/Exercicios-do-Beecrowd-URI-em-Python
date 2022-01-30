qtdCasos = int(input())
for i in range(qtdCasos):
    numPessoas = int(input())
    idiomasDoGrupo = []
    for t in range(numPessoas):
        idiomasDoGrupo.append(input())
    if idiomasDoGrupo.count(idiomasDoGrupo[0]) != len(idiomasDoGrupo):
        print('ingles')
    else:
        print(idiomasDoGrupo[0])
