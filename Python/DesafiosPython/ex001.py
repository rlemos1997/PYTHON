velocidade = float(input("Qual foi a sua velocidade?"))
limite = 80
velocidade_ultrapassada = velocidade - limite

if velocidade > limite:
    print(f"Você foi multado, a sua multa é de R${velocidade_ultrapassada * 7}")
else:
    print("Sem multa")