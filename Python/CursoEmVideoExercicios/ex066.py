soma = 0

while True:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    soma = soma + num

print(f"A soma dos numerod foi de: {soma}")