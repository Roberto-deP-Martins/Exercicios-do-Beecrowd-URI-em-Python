x, y = map(int, input().split())
while x != y:  # Programa encerra quando x for igual y
    if x > y:  # Primeiro maior que segundo: ordem decrescente
        print('Decrescente')
    else:
        print('Crescente')  # Caso contrário a ordem é crescente
    x, y = map(int, input().split())
