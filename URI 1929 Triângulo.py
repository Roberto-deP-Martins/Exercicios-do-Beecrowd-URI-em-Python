# Através do cálculo de combinação (n! / k! x (n - k)!), conclui-se que existem 4 combinações de lados
# Logo, 4 verificações para a Condição de Existência do Triângulo
a, b, c, d = map(int, input().split())
if (a + b > c) and (b + c > a) and (a + c > b):  # ABC
    print('S')
elif (a + b > d) and (b + d > a) and (a + d > b):  # ABD
    print('S')
elif (b + c > d) and (b + d > c) and (c + d > b):  # BCD
    print('S')
elif (c + d > a) and (c + a > d) and (d + a > c):  # CDA
    print('S')
else:
    print('N')
