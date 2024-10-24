ano_nasc = int(input("Digite sua data de nascimento "))
idade = 2024 - ano_nasc

if idade <= 9:
    print(f" Você tem {idade} anos, sua classe é MIRIM")
elif idade <= 14:
    print(f"VOcÊ tem {idade} anos, Sua classe é INFANTIL")
elif idade <= 19:
    print(f"Você tem {idade} anos, sua classe é JUNIOR")
elif idade <= 25:
    print(f"Você tem {idade} anos, sua classe é SENIOR")
else:
    print(f"VocÊ tem {idade} anos, sua classe é MASTER") 