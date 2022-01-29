qtdCasos = int(input())
for i in range(qtdCasos):
    texto = input()
    deslocamento = int(input())  # Quantos caracteres à esquerda deve-se deslocar uma letra
    decriptado = ''  # Texto decriptado
    for letra in texto:
        # Caso o valor seja menor que 65 ('A'), precisa-se adicionar 26 para "dar a volta no alfabeto"
        if (ord(letra) - deslocamento) < 65:
            decriptado = decriptado + (chr((ord(letra) - deslocamento) + 26))  # Adiciona a letra à string
        else:  # Caso contrário, só se adiciona a letra com o deslocamento à string
            decriptado = decriptado + (chr((ord(letra) - deslocamento)))
    print(decriptado)
