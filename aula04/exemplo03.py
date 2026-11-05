pontos = int(input('informe os pontos: '))

if pontos >= 100:
    pontos = pontos + 10
    print(f'execelente! voce tem {pontos} agora!')
elif pontos >= 50:
    pontos = pontos + 5
    print(f'bom desempenho voce tem {pontos} agora!')

else:
     print(f'não desanime, vc esta começando. seus pontos: {pontos}')