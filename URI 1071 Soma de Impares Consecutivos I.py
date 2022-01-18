x = int(input())
y = int(input())
lista = []
if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = x
menor +=1
for i in range(menor, maior):
    if menor % 2 != 0:
        lista.append(menor)
    menor += 1
print(sum(lista))