pessoas = []

for i in range(1,6):
    peso = float(input(f"Digite o peso da {i}º pessoa: "))
    pessoas.append(peso)
    
print(f"A pessoa mais pesada pesa {max(pessoas)}KG")
print(f"A pessoa mais leve pesa {min(pessoas)}KG")