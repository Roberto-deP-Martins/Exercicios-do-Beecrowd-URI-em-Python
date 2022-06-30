class porcao:
    def __init__(self, qtd, tamanho):
        self.qtd = qtd
        self.tamanho = tamanho

total_mandioca = 0
lista_porcoes = [porcao(int(input()), 300), porcao(int(input()), 1500), porcao(int(input()), 600), porcao(int(input()), 1000), porcao(int(input()), 150), porcao(1, 225)]
for objeto in lista_porcoes:
    total_mandioca += objeto.qtd * objeto.tamanho
print(total_mandioca)