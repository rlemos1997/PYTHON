print("=" * 30)
print("10 TERMOS DE UMA PA")
print("=" * 30)

num = int(input("Digite o primeiro termo "))
raz = int(input("Razão: "))
dec = num + (10 - 1) * raz

for i in range(num ,dec + raz , raz):
    print(i, end=" --> ")
print("ACABOU!")
