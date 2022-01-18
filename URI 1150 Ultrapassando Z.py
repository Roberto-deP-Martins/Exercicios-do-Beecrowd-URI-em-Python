x = int(input())
z = -9 ** 999
while z <= x:
    z = int(input())  # Repete até o usuário digitar um valor maior que x para z
lista = []
repeticoes = 0
numero = 0
while sum(lista) < z:  # Enquanto a soma das somas não for z, ela continuará sendo calculada e contará ocorrências disso
    repeticoes += 1
    lista.append(x + numero)
    numero += 1
print(repeticoes)