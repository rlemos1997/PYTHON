num = 0

soma = 0

while True:
    num = int(input("Digite um numero [999 se quiser parar] "))
    if num == 999:
        break
    soma = soma + num

print(f"A soma dos numeros foi de {soma}")