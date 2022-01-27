r = int(input(), 16)
g = int(input(), 16)
b = int(input(), 16)
qtd = (r // g) ** 2
qtd += ((g // b) ** 2) * qtd
qtd = hex(qtd + 1)[2:]
print(qtd)
