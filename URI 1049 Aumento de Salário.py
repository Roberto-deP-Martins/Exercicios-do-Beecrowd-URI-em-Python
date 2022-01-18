salarioAtual = float(input())
if salarioAtual <= 400.00:
    salarioNovo = salarioAtual * 1.15
    reajuste = salarioAtual * 0.15
    percentual = 15
    print('Novo salario:', "%.2f" % salarioNovo)
    print('Reajuste ganho:', "%.2f" % reajuste)
    print('Em percentual: {} %'.format(percentual))
elif 400.01 <= salarioAtual <= 800:
    salarioNovo = salarioAtual * 1.12
    reajuste = salarioAtual * 0.12
    percentual = 12
    print('Novo salario:', "%.2f" % salarioNovo)
    print('Reajuste ganho:', "%.2f" % reajuste)
    print('Em percentual: {} %'.format(percentual))
elif 800.01 <= salarioAtual <= 1200.00:
    salarioNovo = salarioAtual * 1.10
    reajuste = salarioAtual * 0.10
    percentual = 10
    print('Novo salario:', "%.2f" % salarioNovo)
    print('Reajuste ganho:', "%.2f" % reajuste)
    print('Em percentual: {} %'.format(percentual))
elif 1200.01 <= salarioAtual <= 2000.00:
    salarioNovo = salarioAtual * 1.07
    reajuste = salarioAtual * 0.07
    percentual = 7
    print('Novo salario:', "%.2f" % salarioNovo)
    print('Reajuste ganho:', "%.2f" % reajuste)
    print('Em percentual: {} %'.format(percentual))
else:
    salarioNovo = salarioAtual * 1.04
    reajuste = salarioAtual * 0.04
    percentual = 4
    print('Novo salario:', "%.2f" % salarioNovo)
    print('Reajuste ganho:', "%.2f" % reajuste)
    print('Em percentual: {} %'.format(percentual))
