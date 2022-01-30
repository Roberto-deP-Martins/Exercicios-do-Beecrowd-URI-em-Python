num_bandejas = int(input())
copos_derrubados = 0
for i in range(num_bandejas):
    num_latas, num_copos = map(int, input().split())
    if num_latas > num_copos:
        copos_derrubados += num_copos
print(copos_derrubados)
