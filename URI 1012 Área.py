a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
triangulo = (a * c) / 2
print('TRIANGULO: {}'.format("%.3f" % triangulo))
circulo = 3.14159 * (c ** 2)
print('CIRCULO: {}'.format("%.3f" % circulo))
trapezio = ((a + b) * c) / 2
print('TRAPEZIO: {}'.format("%.3f" % trapezio))
quadrado = b ** 2
print('QUADRADO: {}'.format("%.3f" % quadrado))
retangulo = a * b
print('RETANGULO: {}'.format("%.3f" % retangulo))