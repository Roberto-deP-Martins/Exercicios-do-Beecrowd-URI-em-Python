def executa_comandos(pos, sequencia_comandos, novo_comando):
    comando_efetuado = False
    while not comando_efetuado:
        if novo_comando == 'LEFT':
            pos -= 1
            comando_efetuado = True
        elif novo_comando == 'RIGHT':
            pos += 1
            comando_efetuado = True
        else:
            novo_comando = sequencia_comandos[int(novo_comando.split()[2]) - 1]
    return pos


qtd_casos = int(input())
for i in range(qtd_casos):
    pos_personagem = 0
    comandos = []
    qtd_comandos = int(input())
    for t in range(qtd_comandos):
        comando = input()
        comandos.append(comando)
        pos_personagem = executa_comandos(pos_personagem, comandos, comando)
    print(pos_personagem)
