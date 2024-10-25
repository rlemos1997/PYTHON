adulto = 0
homens = 0
mu_jovens = 0




while True:

    print("=" * 20)
    print("CADASTRE UMA PESSOA")
    print("=" * 20)

    idade = int(input("Idade: "))
    if idade > 18:
        adulto = adulto + 1
        

    sexo = str(input("Sexo: [M/F] "))
    if sexo == "M":
        homens = homens + 1
        

    if idade < 20 and sexo == "F":
       mu_jovens = mu_jovens + 1 
       

    opcao = str(input("Quer continuar? [S/N] "))

    if opcao == "N":
        break

print(f"Total de adultos: {adulto}")
print(f"Total de homens {homens}")
print(f" Total de mulheres com menos de 20 anos: {mu_jovens}")


