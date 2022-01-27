msg = input()
vogais = ('a', 'e', 'i', 'o', 'u')
msg_sem_vogal = ''
for letra in msg:
    if letra in vogais:
        msg_sem_vogal += letra
if msg_sem_vogal == msg_sem_vogal[::-1]:
    print('S')
else:
    print('N')