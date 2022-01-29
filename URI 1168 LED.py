qtdCasos = int(input())
# Número é representado por índice, ex: índice 0 corresponde a qtd Leds do número zero, índice 1 do número 1, etc
ledsPorDigito = (6, 2, 5, 5, 4, 5, 6, 3, 7, 6)
for i in range(qtdCasos):
    leds = 0
    numero = input()
    for t in numero:
        leds += ledsPorDigito[int(t)]
    print(leds, 'leds')
