import random
s = 0

for i in range(5):
    num = random.randint(0,50)
    if num % 2 == 0:
        print(num)
        s = s + num

print(f"A soma de todos os pares foi de {s}")