limite = int(input())
operacao = input().split()
if operacao[1] == '+':
    resultado = int(operacao[0]) + int(operacao[2])
elif operacao[1] == '*':
    resultado = int(operacao[0]) * int(operacao[2])
if resultado > limite:
    print('OVERFLOW')
else:
    print('OK')