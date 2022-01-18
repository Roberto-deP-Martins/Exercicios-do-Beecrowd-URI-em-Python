qtdLinhas = int(input())
repeticao = 0
# Todos os três valores iniciais são 1
primeiroValor = 1
segundoValor = 1
terceiroValor = 1
somador = 0  # O valor pelo qual o segundo valor aumenta sempre é no mínimo 1, mas a cada duas
# repetições ele aumenta por 2, 4, 6 e assim sucessivamente, sempre com um aumento de 2 em 2
print(primeiroValor, segundoValor, terceiroValor)
#  O número de linhas impressas sempre será o dobro do valor digitado, entretanto,
#  como a primeira é impressa antes do início do loop, deve se descontá-la do total
for i in range((qtdLinhas * 2) - 1):
    repeticao += 1
    if repeticao == 2:
        somador += 2  # Somador vai sendo incrementado de 2 em 2
        primeiroValor += 1  # O primeiro valor aumenta sempre aparece duas vezes
        segundoValor += somador  # Segundo valor aumenta pelo valor atual do somador cada vez que o primeiro repetir 2x
        terceiroValor = primeiroValor ** 3  # Cada vez que o primeiro valor repetir 2x o terceiro será o primeiro^3
        repeticao = 0  # Repetição volta a ser zero novamente
        print(primeiroValor, segundoValor, terceiroValor)
    else:  # Quando o primeiro valor não tiver se repetido duas vezes os outros dois só aumentam em 1
        segundoValor += 1
        terceiroValor += 1
        print(primeiroValor, segundoValor, terceiroValor)
