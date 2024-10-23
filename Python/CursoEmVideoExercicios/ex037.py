num = int(input("Digite um numero qualquer "))
print("Escolha uma das opções abaixo:")
print("[1] Converter para BINARIO")
print("[2] Converter para OCTAL")
print("[3] COnverter para HEXADECIMAL")

opcao = int(input("Digite a opção: "))

if opcao == 1:
    print(f"O numero {num} convertido para BINARIO é {bin(num)}")

elif opcao == 2:
    print(f" O numero {num} convertido para OCTAL é {oct(num)}")

elif opcao == 3:
    print(f"O numero {num} convertido para HEXADECIMAL é {hex(num)}")

else:
    print("Você precisa digitar uma opção valida")
