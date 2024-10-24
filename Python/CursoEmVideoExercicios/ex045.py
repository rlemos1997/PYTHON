import random
import time

print("Suas opções:")
print("[0] Pedra")
print("[1] Papel")
print("[2] Tesoura")

PEDRA = 0
PAPEL = 1
TESOURA = 2

op_jog = int(input("Qual das opções você vai escolher? "))

op_pc = random.randint(0,2)
time.sleep(1)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO")

print("-=" * 20)
print(f"COMPUTADOR jogou {op_pc}")
print(f"JOGADOR jogou {op_jog}")
print("-=" * 20)

if op_jog == op_pc:
    print("Empatou, jogue novamente!")
    print("-=" * 20)
elif op_jog == 0 and op_pc == 1:
    print("JOGADOR PERDEU!")
    print("-=" * 20)
elif op_jog == 0 and op_pc == 2:
    print("JOGADOR VENCEU!")
    print("-=" * 20)
elif op_pc == 0 and op_jog == 1:
    print("COMPUTADOR PERDEU!")
elif op_pc == 0 and op_jog == 2:
    print("COMPUTADOR VENCEU!")
else:
    print("Entrada invalida")


