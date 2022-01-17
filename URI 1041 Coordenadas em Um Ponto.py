coordenadaX, coordenadaY = map(float, input().split())
if coordenadaX > 0 and coordenadaY > 0:
    print('Q1')
elif coordenadaX > 0 and coordenadaY < 0:
    print('Q4')
elif coordenadaX < 0 and coordenadaY > 0:
    print('Q2')
elif coordenadaX < 0 and coordenadaY < 0:
    print('Q3')
elif coordenadaX == 0 and coordenadaY != 0:
    print('Eixo Y')
elif coordenadaX != 0 and coordenadaY == 0:
    print('Eixo X')
else:
    print('Origem')