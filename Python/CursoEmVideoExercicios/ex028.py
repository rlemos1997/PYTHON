import random
import time

ns = random.randint(1,5)

print("-" * 60)
print("Tente adivinhar o numero que estou pensando entre 1 e 5")
print("-" * 60)


num = int(input("Em que numero eu pensei? "))

print("ANALISANDO...")

time.sleep(1)

if num != ns:
    print("Você errou, mais sorte na próxima vez!")
else:
    print("Acertou Mizeravi, tu é bom mesmo! ")