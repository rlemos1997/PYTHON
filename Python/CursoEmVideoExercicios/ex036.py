valor_casa = int(input("Qual valor da casa? "))

anos_fin = int(input("Em quantos anos sera paga? "))

salario = int(input("Qual o valor do salario? "))

prestacao = valor_casa / (anos_fin * 12)


if prestacao > salario * 0.30:
    print(f"A prestação do financiamento será de R${prestacao:.2f}, infelizmente por conta da sua renda não sera possivel conceder o financiamento")
else:
    print(f"A prestação será de R${prestacao:.2f}, seu financiamento foi CONCEDIDO!")