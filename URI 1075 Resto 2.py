divisor = int(input())
inicio = 0
for i in range(1, 10000):
    inicio += 1
    if inicio % divisor == 2:
        print(inicio)
