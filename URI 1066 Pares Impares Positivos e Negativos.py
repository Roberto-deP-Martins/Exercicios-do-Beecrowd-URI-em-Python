pares = []
impares = []
positivos = []
negativos = []
for i in range(5):
    entrada = int(input())
    if entrada % 2 == 0:
        pares.append(entrada)
        if entrada > 0:
            positivos.append(entrada)
        elif entrada < 0:
            negativos.append(entrada)
    else:
        impares.append(entrada)
        if entrada > 0:
            positivos.append(entrada)
        elif entrada < 0:
            negativos.append(entrada)
print(len(pares), 'valor(es) par(es)')
print(len(impares), 'valor(es) impar(es)')
print(len(positivos), 'valor(es) positivo(s)')
print(len(negativos), 'valor(es) negativo(s)')
