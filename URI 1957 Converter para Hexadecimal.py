def printa_hex(num):
    if num < 10:
        print(num, end='')
    elif num == 10:
        print("A", end='')
    elif num == 11:
        print("B", end='')
    elif num == 12:
        print("C", end='')
    elif num == 13:
        print("D", end='')
    elif num == 14:
        print("E", end='')
    else:
        print("F", end='')
    return None


dec = int(input())
digitos = []
if dec < 16:
    printa_hex(dec)
    print("")
else:
    i = 0
    while dec > 0:
        digitos.append(dec % 16)
        dec //= 16
    for i in digitos[::-1]:
        printa_hex(i)
    print("")