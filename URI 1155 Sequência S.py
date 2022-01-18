divisor = 1
s = 0
while divisor <= 100:  # Divisor aumenta até 100 e vai somando 1 / divisor
    s += 1 / divisor
    divisor += 1
print('%.2f' % s)  # Imprime resultado com duas casas decimais
