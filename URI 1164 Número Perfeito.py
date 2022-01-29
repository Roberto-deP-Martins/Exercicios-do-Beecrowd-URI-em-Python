n = int(input())
for i in range(n):
    x = int(input())
    a = 1
    soma = 0
    while a < x:
        if x % a == 0:
            soma = soma + a
        a = a + 1
    if soma == x:
        print(x, "eh perfeito")
    else:
        print(x, "nao eh perfeito")