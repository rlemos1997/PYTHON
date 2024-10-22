import random

a1 = input("Primeiro Aluno: ")
a2 = input("Segundo Aluno ")
a3 = input("Terceiro Aluno ")
a4 = input("Quarto Aluno ")

nomes = [a1,a2,a3,a4]

asort = random.choice(nomes)

print(f"O aluno sorteado foi: {asort}")