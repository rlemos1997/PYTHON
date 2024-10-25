lista = []

cont = 0
opcao = "S"

while opcao == "S":
    num = int(input("Digite um numero? "))
    opcao = input("Quer continuar? [S/N]? ")
    lista.append(num)
    cont = cont + 1

if opcao == "N":
    print("Acabou")

media = sum(lista)/cont
print(f"A media dos numeros foi: {media}")
print(f"O maior numero digitado foi: {max(lista)}")
print(f"O menor numero digitado foi: {min(lista)}")