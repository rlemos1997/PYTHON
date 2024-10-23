ano = int(input("Digite o ano em que vocÊ deseja saber "))

if ano % 4 == 0 and ano % 100 != 0:
    print("Esse ano é BISSEXTO")
else:
    print("Esse ano NÃO é BISSEXUAL")