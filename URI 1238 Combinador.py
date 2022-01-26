def combinacao(string1, string2):
    idx = 0
    if len(string1) >= len(string2):
        menor = string2
    else:
        menor = string1
    combinado = ''
    while idx < len(menor):
        combinado += string1[idx] + string2[idx]
        idx += 1
    if len(string1) >= len(string2):
        combinado += string1[idx:]
    else:
        combinado += string2[idx:]
    return combinado


qtd_testes = int(input())
for teste in range(qtd_testes):
    palavra1, palavra2 = input().split()
    string_combinado = combinacao(palavra1, palavra2)
    print(string_combinado)