nome = input("Digite seu nome completo ")

print("Analisando seu nome...")
print(f"O seu nome todo em minusculo é: {nome.lower()}")
print(f"O seu nome todo em maiusculo é: {nome.upper()}")
print(f"O seu nome tem um total de {(len(nome) - nome.count(" "))} letras")
print(f"O primeiro nome tem {nome.find(" ")} letras")