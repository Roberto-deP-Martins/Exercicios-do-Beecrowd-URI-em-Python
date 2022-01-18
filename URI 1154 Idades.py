idade = int(input())  # Usuário digita idade
listaIdades = []  # Lista com todas as idades digitadas
while idade >= 0:  # Encerra quando um valor negativo for digitado
    listaIdades.append(idade)  # Adiciona idade à lista
    idade = int(input())
media = sum(listaIdades) / len(listaIdades)
print('%.2f' % media)  # Imprime a média com duas casas decimais
