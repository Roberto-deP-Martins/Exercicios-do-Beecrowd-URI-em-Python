# Subprogramas
def frequencia(e):
    for t in e:
        contagem = valoresDigitados.count(t)  # Conta o número de elementos
        print(f'{t} aparece {contagem} vez(es)')
    return None


# Programa Principal
qtdValores = int(input())
valoresDigitados = []
valoresSemRepetidos = []
for i in range(qtdValores):
    valoresDigitados.append(int(input()))
for numero in valoresDigitados:
    if numero not in valoresSemRepetidos:
        valoresSemRepetidos.append(numero)
valoresDigitados.sort()
valoresSemRepetidos.sort()
frequencia(valoresSemRepetidos)
