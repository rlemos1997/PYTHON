lista = []

num = int(input("Primeiro numero "))
lista.append(num)

num = int(input("segundo numero "))
lista.append(num)

num = int(input("terceiro numero "))
lista.append(num)

print(f"O maior numero digitado foi:{max(lista)}")
print(f"O menor numero digitado foi:{min(lista)}")