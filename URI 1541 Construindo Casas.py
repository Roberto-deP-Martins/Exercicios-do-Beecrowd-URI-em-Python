def regraDeTres(a, p):  # Faz a regra de três após a multiplicação inicial
    total = a * 100 / p
    return total


entrada = input()
while entrada != '0':  # Termina quando o usuário digita 0
    base, altura, porcentagem = map(int, entrada.split())
    area = base * altura
    areaTerreno = regraDeTres(area, porcentagem)
    ladoTerreno = int(areaTerreno ** (1/2))  # Raiz quadrada arredondada para baixo
    print(ladoTerreno)
    entrada = input()
