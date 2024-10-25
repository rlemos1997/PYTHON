import time

print("=" * 30)
print("CAIXA ELETRÔNICO DO SEU ZÉ")
print("=" * 30)

valor = int(input("Qual o valor que você deseja sacar? "))
print("=" * 30)

troco100 = valor // 100
sobra100 = valor % 100

print("Contando cédulas...")
time.sleep(2)


print(f"total de {troco100} notas de R$100 ")


troco50 = sobra100 // 50
sobra50 = sobra100 % 50


print(f"total de {troco50} notas de R$50 ")

troco20 = sobra50 // 20
sobra20 = sobra50 % 20

print(f"Total de {troco20} notas de R$20")

troco10 = sobra20 // 10
sobra10 = sobra20 % 10

print(f"Total de {troco10} notas de R$10")

troco5 = sobra10 // 5
sobra5 = sobra10 % 5

print(f"Total de {troco5} notas de R$5")

troco1 = sobra5 // 1
sobra1 = sobra5 % 1

print(f"Total de {troco1} notas de R$1")

print("=" * 30)
print("Volte Sempre!")
print("=" * 30)