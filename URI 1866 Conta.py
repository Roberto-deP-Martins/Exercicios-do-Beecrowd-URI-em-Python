# Pela estrutura da conta, número de termos par sempre resultará em 0, e número de termos ímpares resultará em 1

qtdCasos = int(input())
for i in range(qtdCasos):
    qtdTermos = int(input())
    if qtdTermos % 2 == 0:
        print('0')
    else:
        print('1')
