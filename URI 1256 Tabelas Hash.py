def mostra_hash(lista):
    idx = 0
    for t in lista:
        if t == [0]:
            print(f'{idx} -> \\')
        else:
            print(f'{idx} -> ', end='')
            if len(t) == t.count(t[0]):
                for i in range(len(t)):
                    if i != len(t) - 1:
                        print(f'{t[i]} -> ', end=''.rstrip())
                    else:
                        print(f'{t[i]} -> \\'.rstrip())
            else:
                for y in range(len(t)):
                    if y != (len(t) - 1):
                        print(f'{t[y]} -> ', end= ''.rstrip())
                    else:
                        print(f"{t[y]} -> \\", end='\n')
        idx += 1
    return None



qtd_testes = int(input())
for num_teste in range(qtd_testes):
    qtd_enderecos_base, qtd_chaves = map(int, input().split())
    chaves = (int(x) for x in input().split())
    lista_hash = [[0]] * (qtd_enderecos_base)
    for i in chaves:
        if lista_hash[i % qtd_enderecos_base] == [0]:
            lista_hash[i % qtd_enderecos_base] = [i]
        else:
            lista_hash[i % qtd_enderecos_base].append(i)
    mostra_hash(lista_hash)
    if num_teste < qtd_testes - 1:
        print()