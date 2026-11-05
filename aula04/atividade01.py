valor_comp = float(input('qual o valor da compra? R$: '))

if valor_comp >= 250:
    valor_comp = valor_comp - 0.16
    print(f'O valor com desconto é R$: {valor_comp}')

else:
    print(f'valor da compra R$: {valor_comp}')