compra  = float(input('valor da compra: '))
cliente_frequente = input('programa de fidelidade? [S/N]: ').lower()[0]
print(cliente_frequente)

if compra > 100 or cliente_frequente == 's':
    print('recebe o brinde')
else:
    print('sem brinde')
