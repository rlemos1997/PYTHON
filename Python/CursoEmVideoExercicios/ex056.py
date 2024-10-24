nomes = []
idades = []
sexos = []
mais_velho = 0
nome_mais_velho = ""
jovens = 0


for i in range(1,6):
    print(f"----- {i}ºPESSOA -----")
    nome = input("Digite seu nome: ")
    nomes.append(nome)

    sexo = input("Digite seu sexo F/M ")
    sexos.append(sexo)

    idade = float(input("Digite a idade: "))
    idades.append(idade)
    if idade > mais_velho and sexo == "M":
        mais_velho = idade
        nome_mais_velho = nome
    if idade < 20 and sexo == "F":
        jovens = jovens + 1

  


media_idade = sum(idades)/5

print(f"A media de idade do grupo é {media_idade} anos")
print(f"O homem mais velho tem {mais_velho} anos")
print(f"O nome do homem mais velho é: {nome_mais_velho}")
print(f"Tem um total de {jovens} mulheres com menos de 20 anos")



 


    
   




