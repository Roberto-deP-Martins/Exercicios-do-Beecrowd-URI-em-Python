qtdTestes = int(input())
for i in range(qtdTestes):  # Repete qtdTestes vezes
    entrada = input().split()
    if entrada[0] == 'Thor':  # Se a pessoa que levanta é Thor
        print('Y')
    else:
        print('N')  # Caso contrário
