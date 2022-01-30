def qtd_igualdades(vetor):
    igualdades = []  # Contém True para alunos que manterão posição e False para aqueles que mudarão de posição

    for idx in range(len(vetor)):
        if vetor[idx] == sorted(vetor, reverse=True)[idx]:
            igualdades.append(True)
        else:
            igualdades.append(False)
    return igualdades.count(True)


qtd_testes = int(input())
for teste in range(qtd_testes):
    qtd_alunos = int(input())
    fila = [int(nota) for nota in input().split()]
    alunos_pos_certa = qtd_igualdades(fila)
    print(alunos_pos_certa)