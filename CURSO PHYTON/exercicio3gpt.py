calorias_totais = []

while True:
    calorias_refeicao = input("Digite a quantidade de calorias do alimento ou sair para finalizar.")
    if calorias_refeicao.lower() == "sair":
        break

    try:
        calorias_totais.append(int(calorias_refeicao))
    except ValueError:
        print("Digite um numero valido ou sair para finalizar ")

soma_calorias = sum(calorias_totais)
