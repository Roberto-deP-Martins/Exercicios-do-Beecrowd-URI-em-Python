naoDivisiveis = []
x = int(input())
y = int(input())
if x < y:
    while x <= y:
        z = x % 13
        if z != 0:
            naoDivisiveis.append(x)
        x = x + 1
    print(sum(naoDivisiveis))
else:
    while y <= x:
        z = y % 13
        if z != 0:
            naoDivisiveis.append(y)
        y = y + 1
    print(sum(naoDivisiveis))