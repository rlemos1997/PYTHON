lista_vendas = [500 , 1000 ,250, 3000, 1500, 2000, 2500]

meta = 1000
percentual_bonus = 0.1

for venda in lista_vendas:
    if venda > meta:
        bonus = percentual_bonus * venda
    else:
        bonus=0
    print(bonus)


        