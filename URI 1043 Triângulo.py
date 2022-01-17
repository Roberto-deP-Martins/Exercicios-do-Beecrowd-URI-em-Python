# Em um triângulo A soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado.
# Essa propriedade é chamada de desigualdade triangular
def verificarTriangulo(a, b, c):
    # Testes da propriedade de desigualdade triangular onde 0 é False e 1 é True:
    if (a + b) > c:
        teste1 = 1
    else:
        teste1 = 0
    if (a + c) > b:
        teste2 = 1
    else:
        teste2 = 0
    if (b + c) > a:
        teste3 = 1
    else:
        teste3 = 0
# Linhas seguintes do subprograma determinam se o polígono com os pontos digitados é um triângulo ou um trapézio
    if teste1 == 1 and teste2 == 1 and teste3 == 1:
        return 'triangulo'
    else:
        return 'trapezio'


ladoA, ladoB, ladoC = map(float, input().split())
poligono = verificarTriangulo(ladoA, ladoB, ladoC)
if poligono == 'triangulo':
    perimetro = ladoA + ladoB + ladoC
    print('Perimetro = {}'.format('%.1f' % perimetro))
else:
    area = ((ladoA + ladoB) * ladoC) / 2
    print('Area = {}'.format('%.1f' % area))
