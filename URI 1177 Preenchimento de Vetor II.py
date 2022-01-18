def obterValores(e):  # Preenche uma lista com os valores de 0 à t - 1
    valores = []
    x = 0  # Um dos valores na lista
    while len(valores) < e:
        valores.append(x)
        x += 1
    return valores


t = int(input())  # Valor no qual serão baseados os valores da lista
n = []  # Lista que será preenchida
indice = 0
valores = obterValores(t)  # Lista com os valores de 0 à (t - 1)
while len(n) < 1000:
    for i in valores:  # Vai adicionando os itens da lista valores à lista n até que ela contenha 1000 itens
        if len(n) < 1000:  # Necessário para que não ultrapasse 1000 itens na lista enquanto loop for ocorre
            n.append(i)
for i in n:
    print(f'N[{indice}] = {i}')
    indice += 1
