valor_inicial, num_operacoes = map(int, input().split())
dinheiro_Dalia = valor_inicial
dinheiro_Eloi = valor_inicial
dinheiro_Felix = valor_inicial
for i in range(num_operacoes):
    operacao = input().split()
    if operacao[0] == 'C':
        if operacao[1] == 'D':
            dinheiro_Dalia -= int(operacao[2])
        elif operacao[1] == 'E':
            dinheiro_Eloi -= int(operacao[2])
        else:
            dinheiro_Felix -= int(operacao[2])
    elif operacao[0] == 'V':
        if operacao[1] == 'D':
            dinheiro_Dalia += int(operacao[2])
        elif operacao[1] == 'E':
            dinheiro_Eloi += int(operacao[2])
        else:
            dinheiro_Felix += int(operacao[2])
    else:
        if operacao[1] == 'D':
            if operacao[2] == 'E':
                dinheiro_Dalia += int(operacao[3])
                dinheiro_Eloi -= int(operacao[3])
            elif operacao[2] == 'F':
                dinheiro_Dalia += int(operacao[3])
                dinheiro_Felix -= int(operacao[3])
        elif operacao[1] == 'E':
            if operacao[2] == 'D':
                dinheiro_Eloi += int(operacao[3])
                dinheiro_Dalia -= int(operacao[3])
            elif operacao[2] == 'F':
                dinheiro_Eloi += int(operacao[3])
                dinheiro_Felix -= int(operacao[3])
        else:
            if operacao[2] == 'D':
                dinheiro_Felix += int(operacao[3])
                dinheiro_Dalia -= int(operacao[3])
            elif operacao[2] == 'E':
                dinheiro_Felix += int(operacao[3])
                dinheiro_Eloi -= int(operacao[3])
print(dinheiro_Dalia, dinheiro_Eloi, dinheiro_Felix)