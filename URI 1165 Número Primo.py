# Números primos são aqueles que só possuem dois divisores, 1 e si mesmo, logo, qualquer número com mais de 2 divisores
# pode ser classificado como não primo

qtdTestes = int(input())
for i in range(qtdTestes):  # Determina quantas vezes o loop vai rodar
    num = int(input())  # Digita o número que irá se verificar se é primo ou não
    teste = 2
    divisores = [1]  # Contém 1 pois porque núremo é divisível por um, armazena os divisores
    while teste <= num:  # Encerra quando se houver testado todos os números como divisores até o próprio valor digitado
        if num % teste == 0:  # Se é divisor
            divisores.append(teste)
            teste += 1
        else:  # Caso contrário
            teste += 1
    if len(divisores) > 2:  # Se houver mais de dois divisores não é primo
        print(f'{num} nao eh primo')
    else:  # Caso contrário é primo
        print(f'{num} eh primo')