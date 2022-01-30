def define_primo(num):  # Retorna True se é Primo, False se não é
    if (num % 2 == 0 and num != 2) or num == 1:
        return False
    else:
        divisores = []
        for i in range(1, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                divisores.append(i)
                if len(divisores) > 1:
                    return False
            elif len(divisores) > 1:
                return False
        return True  # Só ocorre se não chegar em nenhum return primeiro

numero = input()
while numero != '':
    numero = int(numero)
    primo = define_primo(numero)
    if not primo:
        print('Nada')
    else:
        primos_do_numero = []
        nao_super = False
        for algarismo in str(numero):
            primos_do_numero.append(define_primo(int(algarismo)))
            if False in primos_do_numero:  # Se existe algorismo do número que não forem primos
                print('Primo')
                nao_super = True
                break
        if not nao_super:
            print('Super')
    try:        
        numero = input()
    except EOFError:
        break