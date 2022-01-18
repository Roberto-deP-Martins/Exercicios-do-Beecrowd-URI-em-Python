entradas = input().split()  # Pode sair colocando valor, até os que não serão utilisado devido aos critérios
entradas = [int(i) for i in entradas]  # Converte as entradas para int
lista = []
numero = 0
a = entradas[0]  # O valor de a sempre é o primeiro elemento, pois ele pode assumir qualquer valor
entradas[0] = 0  # n não pode assumir 0, por isso impede que assuma o valor de a
for i in entradas:
    if i > 0:  # n só assume valores maiores que 0
        n = i
for i in range(n):  # Faz soma até o valor n - 1
    lista.append(a + numero)  # Põe essas somas na lista
    numero += 1
print(sum(lista))  # Dá a soma de todos as somas