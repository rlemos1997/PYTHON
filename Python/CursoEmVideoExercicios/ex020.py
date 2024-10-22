import random

a1 = input("Primeiro Aluno ")
a2 = input("Segundo Aluno ")
a3 = input("Terceiro Aluno ")
a4 = input("Terceiro Aluno ")

nomes = [a1,a2,a3,a4]

random.shuffle(nomes)

print(nomes)