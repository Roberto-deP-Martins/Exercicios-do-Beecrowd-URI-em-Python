x = 1
while x == 1:
    senha = int(input())
    if senha != 2002:
        print("Senha Invalida")
    if senha == 2002:
        x = x - 1
        print("Acesso Permitido")