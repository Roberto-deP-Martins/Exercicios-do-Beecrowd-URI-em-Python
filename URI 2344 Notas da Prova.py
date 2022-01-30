nota_numerica = int(input())
if nota_numerica == 0:
    print('E')
elif 1 <= nota_numerica <= 35:
    print('D')
elif 36 <= nota_numerica <= 60:
    print('C')
elif 61 <= nota_numerica <= 85:
    print('B')
else:
    print('A')
