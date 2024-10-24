import time




n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

print("    [ 1 ] Somar")
print("    [ 2 ] Multiplicar")
print("    [ 3 ] Maior")
print("    [ 4 ] Novos Numeros")
print("    [ 5 ] Sair do programa")

opcao = int(input("Qual a opção você deseja? "))

while opcao != 5:
    if opcao == 1:
        print(f"A soma entre {n1} + {n2} é: {n1 + n2} ")
        print("="*30)
        time.sleep(1)
    
        print("    [ 1 ] Somar")
        print("    [ 2 ] Multiplicar")
        print("    [ 3 ] Maior")
        print("    [ 4 ] Novos Numeros")
        print("    [ 5 ] Sair do programa")

        opcao = int(input("Qual a opção você deseja? "))
    
    if opcao == 2:
        print(f"A multiplicação entre {n1} e {n2} é igual a: {n1 * n2}")
        print("="*30)
        time.sleep(1)

        print("    [ 1 ] Somar")
        print("    [ 2 ] Multiplicar")
        print("    [ 3 ] Maior")
        print("    [ 4 ] Novos Numeros")
        print("    [ 5 ] Sair do programa")

        opcao = int(input("Qual a opção você deseja? "))

    if opcao == 3:
        print(f"O maior numero entre {n1} e {n2} é: {max(n1,n2)}")
        print("="*30)
        time.sleep(1)

        print("    [ 1 ] Somar")
        print("    [ 2 ] Multiplicar")
        print("    [ 3 ] Maior")
        print("    [ 4 ] Novos Numeros")
        print("    [ 5 ] Sair do programa")

        opcao = int(input("Qual a opção você deseja? "))

    if opcao == 4:
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o segundo numero: "))

        print("="*30)
        time.sleep(1)

        print("    [ 1 ] Somar")
        print("    [ 2 ] Multiplicar")
        print("    [ 3 ] Maior")
        print("    [ 4 ] Novos Numeros")
        print("    [ 5 ] Sair do programa")


        opcao = int(input("Qual a opção você deseja? "))

    if opcao == 5:
        break

    if opcao > 5:

        print("    [ 1 ] Somar")
        print("    [ 2 ] Multiplicar")
        print("    [ 3 ] Maior")
        print("    [ 4 ] Novos Numeros")
        print("    [ 5 ] Sair do programa")

        opcao = int(input("Digite uma opção Valida "))

print("Programa Encerrado!")

        

