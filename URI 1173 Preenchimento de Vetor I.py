# Subprogramas
def preenchimento(lista):
    indice = 0
    while indice != 9:  # Enquanto não se adicionar os 9 itens seguintes do vetor
        lista.append(lista[indice] * 2)  # Anterior * 2
        indice += 1
    return lista


# Programa Principal
i = 0
vetor = [0]
vetor[0] = int(input())
vetor = preenchimento(vetor)
for t in vetor:
    print(f'N[{vetor.index(t)}] = {t}')
