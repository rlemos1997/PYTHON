frase = str(input("Digite uma frase ").lower())

print(f"A letra A aparece {frase.count("a")} vezes")

print(f"A letra A aparece na posição {frase.find("a") +1}")

print(f"A ultima letra A aparece na posição {frase.rfind("a") + 1}")

