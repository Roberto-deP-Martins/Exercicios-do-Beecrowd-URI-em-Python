def mostrar_vetor(vetor, par):
    indice = 0
    if par:
        for i in vetor:
            print(f'par[{indice}] = {i}')
            indice += 1
    else:
        for i in vetor:
            print(f'impar[{indice}] = {i}')
            indice += 1
    return None


def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


pares = []
impares = []
nums_digitados = 0
while nums_digitados < 15:
    entrada = int(input())
    nums_digitados += 1
    if eh_par(entrada):
        if len(pares) == 5:  # Quando chegar em 5 itens imprime vetor
            mostrar_vetor(pares, eh_par(entrada))
            pares = [entrada]
        else:
            pares.append(entrada)
    else:
        if len(impares) == 5:
            mostrar_vetor(impares, eh_par(entrada))
            impares = [entrada]
        else:
            impares.append(entrada)
if len(impares) != 0:
    mostrar_vetor(impares, False)
if len(pares) != 0:
    mostrar_vetor(pares, True)