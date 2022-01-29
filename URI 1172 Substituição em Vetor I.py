# Subprogramas
def substituir(e):
    if e <= 0:
        e = 1
        x.append(e)
    else:
        x.append(e)
    return None


# Programa Principal
x = []
while len(x) != 10:
    entrada = int(input())
    substituir(entrada)
indice = 0
for i in x:
    print(f'X{[indice]} =', i)
    indice += 1
