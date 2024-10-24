import random

tentativas = 0

pc = random.randint(1,10)

print("Sou seu computador, ta afim de um jogo de adivinha? ")
print("Tente adivinhar o numero que estou pensando de 1 a 10...")

eu = int(input("Qual o seu palpite? "))

while pc != eu:
    if eu > pc:
        eu = int(input("Menos... Tente de novo campeão! "))
        tentativas = tentativas + 1
    else:
        eu = int(input("Mais... Tente de novo campeão! "))
        tentativas = tentativas + 1

print(f"ACERTOU MIZERAVI, em {tentativas} tentativas")