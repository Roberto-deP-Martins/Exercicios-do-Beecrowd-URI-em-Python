qtdTestes = int(input())  # Qtd de vezes que o programa vai rodar
for i in range(qtdTestes):  # Repete o programa
    texto = input()
    textoConstrucao = ''  # String vazia pra fazer modificações da original por serem imutáveis
    for t in texto:
        if t.isalpha():  # Se for uma letra
            # Põe na string a letra deslocada 3 posições à direita no alfabeto
            textoConstrucao = textoConstrucao + chr(ord(t) + 3)
        else:  # Põe na string o restante dos caracteres
            textoConstrucao = textoConstrucao + t
    texto = textoConstrucao  # Retorna o conteúdo a string original
    texto = texto[::-1]  # Inverte a string
    textoConstrucao = texto[:len(texto) // 2]  # Pega a segunda metade da string
    for w in texto[len(texto) // 2:]:  # Percorre a primeira metade da outra string
        textoConstrucao = textoConstrucao + chr(ord(w) - 1)  #
    print(textoConstrucao)