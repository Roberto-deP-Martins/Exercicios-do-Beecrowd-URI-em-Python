comando = 1
while comando == 1:
    notas = []
    while len(notas) != 2:  # Faz a média assim que tiver dois números na lista
        nota = float(input())
        if 0 <= nota <= 10:  # Só entra na lista números válidos (presentes no intervalo [0,10]
            notas.append(nota)
        else:
            print('nota invalida')
    media = sum(notas) / len(notas)
    print('media = {}'.format('%.2f' % media))
    segundoComando = 4  # Qualquer número diferente de 1 e 2 funciona pra não quebrar o loop
    while segundoComando != 1:  # Se esse valor assumir 1 o programa inteiro se repete
        print('novo calculo (1-sim 2-nao)')
        comando = int(input())
        segundoComando = comando
        if segundoComando == 2:  # 2 encerra o programa
            break
        elif segundoComando == 1:
            None
        else:  # O valro não ser 1 ou 2 repete a pergunta até que o usuário digite 1 ou 2
            segundoComando = 0
