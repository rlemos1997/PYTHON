import random

num = random.randint(1,9999)

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f"Analisando o numero {num}...")


print("-=" * 20)
print(f"a unidade de {num} é {u}")
print(f"A dezeza de {num} é {d}")
print(f"A centena de {num} é {c}")
print(f"O milhar de {num} é {m}")
print("-=" * 20)