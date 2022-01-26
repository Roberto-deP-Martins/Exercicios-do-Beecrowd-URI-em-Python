qtd_testes = int(input())
for i in range(qtd_testes):
    a, b = input().split()
    if a[len(a) - len(b):] == b:
        print('encaixa')
    else:
        print('nao encaixa')