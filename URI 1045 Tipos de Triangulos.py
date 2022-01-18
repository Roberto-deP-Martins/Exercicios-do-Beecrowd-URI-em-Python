lista = input().split()
lista = [float(i) for i in lista]
lista.sort(reverse=True)  # Organiza em ordem decrescente
a, b, c = lista[0], lista[1], lista[2]
if a >= (b + c):
    print('NAO FORMA TRIANGULO')
elif (a ** 2) == ((b ** 2) + (c ** 2)):
    print('TRIANGULO RETANGULO')
    # Se um dos dois lados estiver presente duas vezes na lista, o triângulo é isósceles
    if lista.count(lista[0]) == 2 or lista.count(lista[1]) == 2:
        print('TRIANGULO ISOSCELES')
    # Triângulos retângulos não podem ser equiláteros
elif (a ** 2) > ((b ** 2) + (c ** 2)):
    print('TRIANGULO OBTUSANGULO')
    if lista.count(lista[0]) == 2 or lista.count(lista[1]) == 2:
        print('TRIANGULO ISOSCELES')
    elif a == b == c:
        print('TRIANGULO EQUILATERO')
elif (a ** 2) < ((b ** 2) + (c ** 2)):
    print('TRIANGULO ACUTANGULO')
    if lista.count(lista[0]) == 2 or lista.count(lista[1]) == 2:
        print('TRIANGULO ISOSCELES')
    elif a == b == c:
        print('TRIANGULO EQUILATERO')
