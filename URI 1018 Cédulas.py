valor = int(input())
print(valor)
notas = (100, 50, 20, 10, 5, 2, 1)
t = valor
for i in notas:
    if valor // i > 0:
        print(f'{valor // i} nota(s) de R$ {i},00')
        valor = valor - (i * (valor // i))
    else:
        print(f'0 nota(s) de R$ {i},00')