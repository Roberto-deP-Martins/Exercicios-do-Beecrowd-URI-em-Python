#  A sequência de Fibonacci é uma sequência onde cada número, após os 2
#  primeiros (0, 1), é igual à soma dos 2 anteriores.


listaFibonacci = [0, 1]  # A lista sempre começa com 0 e 1
qtdNumeros = int(input()) - 2  # Descontar o 0 e 1 já presentes na lista Fibonacci
indice = 1  # Começa no segundo (1) pois já há dois na lista
for i in range(qtdNumeros):  # Enquanto a lista não tiver a quantidade de números digitadas loop continua
    listaFibonacci.append((listaFibonacci[indice - 1] + listaFibonacci[indice]))  # Põe a soma dos 2 anteriores na lista
    indice += 1  # Avança o índice na lista ao qual a linha anterior vai se referir
print(*listaFibonacci)  # imprime a sequência de Fibonacci
