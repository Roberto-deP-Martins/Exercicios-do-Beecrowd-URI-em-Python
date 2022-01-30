while True:
    try:
        reclamacoes = int(input())
        if reclamacoes == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except EOFError:
        break
