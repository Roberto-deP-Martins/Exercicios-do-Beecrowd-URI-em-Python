tradutor = {}
id_ascii = 97  # código ascii para 'a'
permutacao = input()

# chr(id_ascii) vai pôr cada letra do alfabeto (de 97 até 97 + 26, ou seja, a até z) como key no dicionário e cada uma terá sua correspondência
for letra in permutacao:  # As 26 letras do alfabetp
    tradutor[chr(id_ascii)] = letra
    id_ascii += 1
msg = input()
msg_traduzida = ''
for letra in msg:
    msg_traduzida += tradutor[letra]
print(msg_traduzida)