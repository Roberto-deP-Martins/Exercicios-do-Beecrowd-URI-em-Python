# Subprogramas
def selecionar(e):
    indice = 0
    for i in e:
        if i <= 10:
            print(f'A[{indice}] = {i}')
        indice += 1
    return None


# Programa Principal
vetor = []
while len(vetor) < 100:
    vetor.append(float(input()))
selecionar(vetor)
