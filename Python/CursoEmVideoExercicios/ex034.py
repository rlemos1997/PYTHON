salario = int(input("Digite seu salario "))

if salario < 1250:
    print(f"Quem ganhava R${salario}, agora vai ganhar R${salario * 1.15:.2f}")
else:
    print(f"Quem ganhava R${salario}, agora vai ganhar R${salario * 1.10:.2f}")