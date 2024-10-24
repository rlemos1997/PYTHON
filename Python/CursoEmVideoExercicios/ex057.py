sexo = (input("Digite seu sexo [M/F] ")).strip().upper()

while sexo != "M" and sexo != "F":
    sexo = input("Dados invalidos. Por favor informe seu sexo: ")
print(f"Sexo {sexo} cadastrado com sucesso!")
    
