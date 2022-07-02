class Porcao:
    def __init__(self, qtd, tamanho):
        self.qtd = qtd
        self.tamanho = tamanho

total_mandioca = 0
lista_porcoes = [Porcao(int(input()), 300), Porcao(int(input()), 1500), Porcao(int(input()), 600), Porcao(int(input()), 1000), Porcao(int(input()), 150), Porcao(1, 225)]
for objeto in lista_porcoes:
    total_mandioca += objeto.qtd * objeto.tamanho
print(total_mandioca)