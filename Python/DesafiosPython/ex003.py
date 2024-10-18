import random

numero_sorteado = random.randint(0, 10)
numero = int(input("Tente adivinhar o número de 0 a 10: "))

while numero != numero_sorteado:
    if numero > numero_sorteado:
        print("DIgite um numero menor")
        numero = int(input("Tente adivinhar o número de 0 a 10: "))
    if numero < numero_sorteado:
        print("DIgite um numero maior")
        numero = int(input("Tente adivinhar o número de 0 a 10: "))

print("Parabens, voce acertou")



58