for i in range(int(input())):
    x, y = map(int, input().split())
    if y == 0:
        print('divisao impossivel')
    else:
        divisao = x / y
        print('%.1f' % divisao)