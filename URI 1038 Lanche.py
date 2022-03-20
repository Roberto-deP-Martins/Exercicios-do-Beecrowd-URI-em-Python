listaProdutos = (4.00, 4.50, 5.00, 2.00, 1.50)  # Indice 0 = Item 1, Indice 1 = Item 2,...
produto, qtd = map(int, input().split())
total = qtd * listaProdutos[produto - 1]  # Indice sempre será 1 a menos que o numero do indice( que é o valor digitado)
print('Total: R$ {}'.format("%.2f" % total))
