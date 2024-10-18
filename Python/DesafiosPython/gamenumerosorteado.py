import random

numero_sorteado = random.randint(0, 10)
tentativas = int(input("Digite quantas tentativavocÊ quer"))
numero = int(input("Tente adivinhar o número de 0 a 10: "))
palpites = 1


while numero != numero_sorteado and palpites < tentativas:
    if numero > numero_sorteado:
        palpites += 1
        print("DIgite um numero menor")
        print(f"VOcê ainda tem {tentativas + 1 - palpites} tentativas")
        numero = int(input("Tente adivinhar o número de 0 a 10: "))
    
    if numero < numero_sorteado:
        palpites += 1
        print("DIgite um numero maior")
        print(f"VOcê ainda tem {tentativas + 1 - palpites} tentativas")
        numero = int(input("Tente adivinhar o número de 0 a 10: "))

if palpites >= 5:
    print("Você perdeu")
else:
    print(f"Parabens, voce acertou em {palpites} tentativas")
