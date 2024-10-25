primeiro = int(input("Primeiro termo: "))
razao = int(input("Razão: "))

termo = primeiro
cont = 1 
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} ->", end=" " )
        termo = termo + razao
        cont = cont + 1

    print("PAUSA")
    mais = int(input("Mais quantos termos você quer mostrar? "))

print("PROGRAMA FINALIZADO")
