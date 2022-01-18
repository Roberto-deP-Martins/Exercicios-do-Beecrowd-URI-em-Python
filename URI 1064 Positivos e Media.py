qtdPositivos = 0
somaPositivos = 0
for i in range(6):
    entrada = float(input())
    if entrada > 0:
        qtdPositivos += 1
        somaPositivos += entrada
media = somaPositivos / qtdPositivos
print(f'{qtdPositivos} valores positivos')
print(f'{media:.1f}')