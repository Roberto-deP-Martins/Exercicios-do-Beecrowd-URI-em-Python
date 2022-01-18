denominador = 1
s = 0
numerador = 1
while numerador <= 39:  # Sequência termina com 39/?
    s += numerador / denominador  # Divisão que dá valor à s
    numerador += 2  # Numerador aumenta de 2 em 2
    denominador *= 2  # Divisor aumenta de 2 em 2
print('%.2f' % s)  # Imprime o resultado com 2 casas decimais
