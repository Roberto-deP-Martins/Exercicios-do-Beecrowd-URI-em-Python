codPeca1, qtdPeca1, valorPeca1 = input().split()
codPeca1, qtdPeca1 = int(codPeca1), int(qtdPeca1)
valorPeca1 = float(valorPeca1)
codPeca2, qtdPeca2, valorPeca2 = input().split()
codPeca2, qtdPeca2 = int(codPeca2), int(qtdPeca2)
valorPeca2 = float(valorPeca2)
totalPeca1 = qtdPeca1 * valorPeca1
totalPeca2 = qtdPeca2 * valorPeca2
total = totalPeca1 + totalPeca2
print('VALOR A PAGAR: R$ {}'.format("%.2f" % total))