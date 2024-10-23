vel = int(input("Qual foi a velocidade do carro? "))

if vel > 80:
    print("Você foi multado cabra")
    print(f"A sua multa é de R${(vel - 80) * 7 }")
else:
    print("Pode seguir, va na paz e dirija com cuidade")