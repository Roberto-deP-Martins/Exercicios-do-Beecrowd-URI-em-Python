notas = input().split()
notas = [float(i) for i in notas]
media = ((2 * notas[0]) + (3 * notas[1]) + (4 * notas[2]) + notas[3]) / (2 + 3 + 4 + 1)
print('Media: {}'.format("%.1f" % media))
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    notaExame = float(input())
    print('Nota do exame: {}'.format("%.1f" % notaExame))
    novaMedia = (notaExame + media) / 2
    if novaMedia >= 5:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: {}'.format("%.1f" % novaMedia))