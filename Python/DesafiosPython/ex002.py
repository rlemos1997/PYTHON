valor_casa = int(input("Qual o valor da casa? "))
salario = int(input("Qual o seu salaírio? "))
anos_fin = int(input("Em quantos anos deseja pagar? "))
meses_fin = anos_fin * 12
prestacao = valor_casa / meses_fin

if prestacao < salario *0.30:
    print(f"Seu financiamento foi aprovado, sua prestação é de {prestacao}! ")
else:
    print("Seu financiamento foi reprovado por falta de margem, sinto muito ")