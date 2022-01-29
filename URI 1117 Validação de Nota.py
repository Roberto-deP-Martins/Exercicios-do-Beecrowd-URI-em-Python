# Subprogramas
def validar(e):
    if e < 0 or nota > 10:
        return False
    else:
        return True


# Programa Principal
listaNotasValidas = []
notasValidasInseridas = 0
while notasValidasInseridas < 2:
    nota = float(input())
    EhValido = validar(nota)
    if not EhValido:
        print('nota invalida')
    else:
        listaNotasValidas.append(nota)
        notasValidasInseridas += 1
media = sum(listaNotasValidas) / 2
print('media =', media)
