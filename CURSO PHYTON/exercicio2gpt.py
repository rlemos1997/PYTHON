calorias_totais = []
refeicoes_totais = int(input("Quantas refeições você irá fazer no dia? "))
#refeicoes_totais = int(refeicoes_totais)
print("Total de refeições: ",refeicoes_totais)

for calorias in range(refeicoes_totais):
    calorias_consumidas = int(input("Digite a quantiadade de calorias: "))
    calorias_totais.append(calorias_consumidas)

#calorias_consumidas = int(calorias_consumidas)
soma_calorias_consumidas = sum(calorias_totais)
print("O total das calorias consumidas é:",soma_calorias_consumidas)

if soma_calorias_consumidas >= 2000:
    print("Você consumiu mais calorias do que recomendado")
else:
    print("Você está dentro da quantidade recomendada de calorias")

    