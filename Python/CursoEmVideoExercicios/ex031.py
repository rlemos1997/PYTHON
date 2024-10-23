dist = int(input("Quantos Km terá a sua viagem? "))

if dist < 200:
    print(f"Você ira fazer uma viagem de {dist}KMs")
    print(f"Sua viagem custara um total de R${dist * 0.50}")
else:
    print(f"Sua viagem tera uma distancia de {dist}KMs")
    print(f"Sua viagem custará um total de R${dist * 0.45}")