salario = float(input('informe o seu salario: '))

vendas = float(input('informe o valor de vendas: '))

if vendas >= 1000:
   bonus = 150
   total = bonus + salario
   print(f'Boa! suas vendas foram de: {total:.2f}')

elif vendas >= 500:
   bonus = 75
   total = bonus + salario
   print(f'boa! suas vendas foram de: {total:.2f}')

else:
   print(f'Sinto muito mas voce nao bateu a meta esse mes, seu pagamento sera de apenas: {salario:.2f}')

   

