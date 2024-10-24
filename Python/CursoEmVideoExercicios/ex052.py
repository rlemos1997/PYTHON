num = int(input("Digite um numero: "))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        tot = tot + 1

print(f"O numero {num} foi dividido {tot} vezes")
if tot <= 2:
    print("Esse numero é primo")
else:
    print("Esse numero não é primo")
    