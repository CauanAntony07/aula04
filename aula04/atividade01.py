valor_comp = float(input('qual o valor da compra? R$: '))

if valor_comp > 250:
    desconto = valor_comp * 0.16
    valor_final = valor_comp - desconto
    
    print(f'O valor com desconto é R$: {valor_final:.2f}')

else:
    print(f'valor da compra R$: {valor_comp:.2f}')