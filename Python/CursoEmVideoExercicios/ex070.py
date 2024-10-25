valor_total = 0
mais_mil = 0
opcao = "S"

while True:
    produto = input("Nome do produto: ")
    preco = int(input("Preço do produto: "))

    preco_mais_baixo = preco
    valor_total = valor_total + preco
    produto_mais_barato = produto

    if preco > 1000:
        mais_mil = mais_mil + 1


    if preco < preco_mais_baixo:
        preco_mais_baixo = preco
        produto_mais_barato = produto
        

    opcao = input("Quer continuar? [S/N] ")
    if opcao == "N":
        break    


print(f"Produto mais barato: {produto_mais_barato}")
print(f"Valor total da compra: R${valor_total}")
print(f"Quantidade de produtos que custaram mais de R$1000,00 {mais_mil}")
print(f"Preço mais baixo foi: {preco_mais_baixo}")

print("FIM DO PROGRAMA")