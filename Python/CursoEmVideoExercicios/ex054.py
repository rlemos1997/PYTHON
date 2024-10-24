maior = 0
menor = 0


for i in range(1,8):    
    ano_nasc = int(input(f"em que ano a {i}ª pessoa nasceu? "))
    if ano_nasc < 2006:
        maior = maior + 1
    else:
        menor = menor + 1
    

print(f"Ao todo tivemos {maior} pessoas maiores de idade e um total de {menor} pessoas menores de idade.")
