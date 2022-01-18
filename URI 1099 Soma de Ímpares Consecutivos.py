for i in range(int(input())):  # Dá a quantidade de vezes que o programa será executado
    x, y = map(int, input().split())
    # Seis linhas subsequentes determinam qual dos valores é o maior e qual é o menor
    if x > y:
        maior = x
        menor = y
    else:
        maior = y
        menor = x
    # Se o maior valor for apenas o número seguinte ao menor não haverão inteiros entre eles. O mesmo ocorre caso o
    # menor e o maior número forem iguais
    if (maior - menor) == 1 or maior == menor:
       print(0)
    else:
        numero = ''
        pisoIntervalo = menor
        impares = []
        numeros = []
        while len(numeros) < (maior - menor) - 1:  # Enquanto não se obter todos os números entre o maior e menor
            # Duas linhas subsequentes garantem que obtenha-se os números entre maior e menor
            numero = pisoIntervalo + 1
            pisoIntervalo += 1
            numeros.append(numero)
            if numero % 2 != 0:  # Se o resto for diferente de zero o número é impar
                impares.append(numero)
        print(sum(impares))
