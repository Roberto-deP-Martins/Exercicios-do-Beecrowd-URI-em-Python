repeticoes = 0
t = 8
i = 1
j = 8
while repeticoes != 5:
    while j != (t - 3):
        j -= 1
        print('I={} J={}'.format(i, j))
    j = 8
    i += 2
    repeticoes += 1
