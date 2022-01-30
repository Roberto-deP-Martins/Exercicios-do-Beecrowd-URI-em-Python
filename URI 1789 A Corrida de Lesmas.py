while True:
    try:
        qtdLesmas = int(input())
        velocidadesLesmas = input().split()  # Separa as velocidades (em lista)
        listaLesmas = [int(i) for i in velocidadesLesmas]  # Faz outra lista com os ints dos valores da lista anterior
        listaLesmas.sort()  # Põe em ordem crescente, maior será [-1]
        if listaLesmas[-1] < 10:
            print('1')
        elif 10 < listaLesmas[-1] < 20:
            print('2')
        else:
            print('3')
    except EOFError:  # Encerra em EOF
        break
