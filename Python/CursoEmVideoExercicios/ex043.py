import time

peso = float(input("Digite seu peso "))
altura = float(input("Digite sua altura "))

imc = peso / altura**2

time.sleep(1)

print("analisando seu IMC...")

print(f"Seu IMC é de {imc}")

if imc < 18.5:
    print("VOcÊ está abaixo do peso")
elif 18.5 < imc < 25:
    print("Você está com o peso normal")
elif 25 < imc < 30:
    print("Você está com sobrepeso")
elif 30 < imc < 35:
    print("Você está com obesidade grau 1")
elif 35 < imc < 40:
    print("VOcÊ está com obesidade grau 2")
elif 40 < imc: 
    print("Você está com obesidade grau 3")