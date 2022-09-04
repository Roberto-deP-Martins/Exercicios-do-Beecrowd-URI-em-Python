qtd_abas, num_acoes = map(int, input().split())
for i in range(num_acoes):
    acao = input()
    if acao == "fechou":
        qtd_abas += 1
    else:
        qtd_abas -= 1
print(qtd_abas)