qtdCasos = int(input())
for i in range(qtdCasos):
    entrada = input()
    metade1 = entrada[0:len(entrada) // 2][::-1]  # Primeira metade da string, mas invertida
    metade2 = entrada[len(entrada) // 2:][::-1]  # Segunda metade da string, mas invertida
    print(metade1 + metade2)  # A junção das duas partes
