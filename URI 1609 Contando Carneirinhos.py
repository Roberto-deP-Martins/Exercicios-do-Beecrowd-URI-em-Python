def conta_carneiros(dados_entrada):
    dados_entrada = set(dados_entrada)
    contagem = len(dados_entrada)
    return contagem


qtd_testes = int(input())
for i in range(qtd_testes):
    qtd_carneiros = int(input())
    entrada_carneiros = input().split()
    num_carneiros = conta_carneiros(entrada_carneiros)
    print(num_carneiros)