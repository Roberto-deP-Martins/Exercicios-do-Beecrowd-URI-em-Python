# Subprogramas
def inserirNumeros(lista):
    while len(lista) < 20:
        lista.append(int(input()))
    return lista


def mostrarLista(lista):
    indice = 0  # Necessário para o caso de ter item repetido, que ocasionaria falha no método .index()
    for item in lista:
        print(f'N[{indice}] = {item}')
        indice += 1
    return None


# Programa Principal
vetor = []
vetor = inserirNumeros(vetor)
listaFinal = vetor[::-1]  # Vetor ao contrário
mostrarLista(listaFinal)
