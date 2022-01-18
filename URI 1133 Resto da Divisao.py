x = int(input())
y = int(input())
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = y
for i in range(menor + 1, maior):  # Dá todos os valores entre o menor e maior valor
    # menor + 1 para não incluir o próprio menor, não é necessário digitar
    # maior -1 pois o Python já termina o range no valor anterior ao maior
    if i % 5 == 2 or i % 5 == 3:
        print(i)
