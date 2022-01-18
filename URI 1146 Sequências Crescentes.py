x = int(input())
while x != 0:  # Encerra quando usuário digita 0
    t = 1
    lista = []  # Lista à qual os numeros a serem impressos serão adicionados
    for i in range(x):  # Número de vezes que ocorre depende de x
        lista.append(t)
        t += 1  # Vai aumentando a partir de 1
    print(*lista)
    x = int(input())
