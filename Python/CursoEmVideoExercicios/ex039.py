ano_nasc = int(input("DIgite seu ano de nascimento "))
ano_atual = 2024
idade = ano_atual - ano_nasc

if idade < 18:
    print(f"Você tem {idade} Anos, ainda faltam {18 - idade} anos para você se alistar")
    print(f"Seu alistamento sera no ano de {ano_nasc + 18}")
elif idade == 18:
    print(f"Você já está na idade de se alistar, fique ligado!")
else:
    print(f"Você já tem {idade} anos, deveria ter se alistado no ano de {ano_nasc + 18}")
    print("PRocure se regularizar já soldado!")