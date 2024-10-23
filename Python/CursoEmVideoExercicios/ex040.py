n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1+n2)/2

if media < 5:
    print(f"Sua media é de {media}, você foi REPROVADO!")
elif 5 < media < 6.9:
    print(f"Sua media e´de {media}, você está de RECUPERAÇÃO!")
else:
    print(f"Sua média é de {media}, parabéns você foi APROVADO!")