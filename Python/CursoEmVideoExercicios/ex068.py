import random

eu = 0
pc = 0
vitorias = 0
resultado = "Par"


while True:
    eu = int(input("Digite um numero: "))
    op_eu = input("Par ou Impar? [P/I]")
    pc = random.randint(1,10)

    if (eu + pc) % 2 == 0:
        resultado = "PAR"
    else:
        resultado = "IMPAR"

    print(f"Você jogou {eu} e o PC jogou {pc}, a soma deu {eu + pc}, deu {resultado}")
    
    if op_eu == "P" and resultado == "PAR":
        print("Você venceu!")
        vitorias = vitorias + 1
    elif op_eu == "I" and resultado == "IMPAR":
        print("Você Venceu!")
        vitorias = vitorias + 1
    else:
        print("Você perdeu!")
        break

print(f"GAME OVER, Você venceu {vitorias} vezes!")