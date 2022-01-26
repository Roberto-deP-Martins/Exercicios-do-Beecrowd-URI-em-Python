def produto_do_jogo(string):
    valor1, valor2 = int(entrada[0]), int(entrada[2])
    produto = valor1 * valor2
    return produto


def subtracao_do_jogo(string):
    valor1, valor2 = int(entrada[0]), int(entrada[2])
    diferenca = valor2 - valor1
    return diferenca


def soma_do_jogo(string):
    valor1, valor2 = int(entrada[0]), int(entrada[2])
    total = valor1 + valor2
    return total


qtd_testes = int(input())
for teste in range(qtd_testes):
    entrada = input()
    if entrada[0] == entrada[2]:
        resultado = produto_do_jogo(entrada)
        print(resultado)
    elif entrada[1].isupper():
        resultado = subtracao_do_jogo(entrada)
        print(resultado)
    else:
        resultado = soma_do_jogo(entrada)
        print(resultado)