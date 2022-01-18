x = int(input())
while x != 0:  # Encerra quando o usuário digita 0
    pares = []  # Lista para armazenar os números pares
    while len(pares) != 5:  # Termina o loop quando obter 5 pares
        if x % 2 == 0:  # Verifica se valor é par
            pares.append(x)
            x += 1
        else:
            x += 1
    print(sum(pares))
    x = int(input())
