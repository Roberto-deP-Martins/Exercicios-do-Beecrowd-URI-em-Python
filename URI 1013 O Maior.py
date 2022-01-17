a, b, c = map(int, input().split())
# A fórmula (a + b + abs(a - b)) / 2 dá o número do maior de dois valores
maiorAB = (a + b + abs(a - b)) / 2  # Diz o maior entre A e B
maior = int((maiorAB + c + abs(maiorAB - c)) / 2)  # Diz se C é maior que algum dos dois primeiros valores
print(f'{maior} eh o maior')
