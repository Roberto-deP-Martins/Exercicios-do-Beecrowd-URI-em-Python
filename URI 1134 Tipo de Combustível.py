# 1 - Álcool, 2 - Gasolina, 3 - Diesel, 4 - Fim
dados = []
print('MUITO OBRIGADO')
combustivel = 0
while combustivel != 4:  # Se o usuário digitar 4 o programa encerra
    combustivel = int(input())
    if combustivel in range(1, 4):  # Pelo modo como range funciona, só está contando de 1 até 3
       dados.append(combustivel)
print('Alcool:', dados.count(1))
print('Gasolina:', dados.count(2))
print('Diesel:', dados.count(3))
