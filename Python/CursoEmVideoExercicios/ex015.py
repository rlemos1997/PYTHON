kmrodado = float(input("Quantos kilometros foram rodados? "))
diasaluguel = int(input("Quantos dias ele ficou alugado? "))

aluguel = diasaluguel * 60
valorkm = kmrodado * 0.15

valortotal = aluguel + valorkm

print(f"O total a pagar é de {valortotal}")