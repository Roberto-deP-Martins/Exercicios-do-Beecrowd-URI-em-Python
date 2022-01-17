from math import sqrt
a, b, c = map(float, input().split())
delta = (b ** 2) - (4 * a * c)
if delta <= 0:
    print('Impossivel calcular')
elif 2 * a == 0:
    print('Impossivel calcular')
else:
    raiz1 = (-b + sqrt(delta)) / (2 * a)
    raiz2 = (-b - sqrt(delta)) / (2 * a)
    print('R1 =',"%.5f" % raiz1)
    print('R2 =',"%.5f" % raiz2)