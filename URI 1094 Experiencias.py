qtdCasos = int(input())
total = []
coelhos = []
ratos = []
sapos = []
for i in range(qtdCasos):
    entrada = input()
    multiplicador = int(entrada[0:2])  # Pega o número de cobais usadas em um experimento
    if 'C' in entrada:
        for t in range(multiplicador):  # Adiciona a cobaia 'coelho' o número de vezes que ela foi usada à lista com todas as cobaias e a lista de coelhos
            coelhos.append('C')
            total.append('C')
    elif 'R' in entrada: # Adiciona a cobaia 'rato' o número de vezes que ela foi usada à lista com todas as cobaias e a lista de ratos
        for t in range(multiplicador):
            ratos.append('R')
            total.append('R')
    else:
        for t in range(multiplicador): # Adiciona a cobaia 'sapo' o número de vezes que ela foi usada à lista com todas as cobaias e a lista de sapos
            sapos.append('S')
            total.append('S')
percentualCoelhos = (len(coelhos) / len(total)) * 100  # Dá o percentual de coelhos em relação ao total de cobaias
percentualRatos = (len(ratos) / len(total)) * 100  # Dá o percentual de ratos em relação ao total de cobaias
percentualSapos = (len(sapos) / len(total)) * 100  # Dá o percentual de sapos em relação ao total de cobaias
print('Total: {} cobaias'.format(len(total)))
print('Total de coelhos: {}'.format(len(coelhos)))
print('Total de ratos: {}'.format(len(ratos)))
print('Total de sapos: {}'.format(len(sapos)))
print('Percentual de coelhos: {} %'.format("%.2f" % percentualCoelhos))
print('Percentual de ratos: {} %'.format("%.2f" % percentualRatos))
print('Percentual de sapos: {} %'.format("%.2f" % percentualSapos))
