lista = ("zero", "um" , "dois", "tres","quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

numero = int(input("digite um numero entre 0 e 20: "))

while True:
    if numero < 0 or numero > 20:
        print("numero invalido")
        numero = int(input("digite um numero entre 0 e 20: "))

    else:
        print(f"numero digitado é: {lista[numero]}")
        numero = int(input("digite um numero entre 0 e 20: "))
    
  
    
        