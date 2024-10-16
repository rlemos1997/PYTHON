#nome = input("Digite seu nome ")
#email = input("Digite seu e-mail ")

#primeiroespaco = nome.find(" ")
#primeironome = nome[:primeiroespaco+1]
#print( f"{primeironome}, esse foi o e-mail inserido {email}, está correto? ")

vendas = [100 , 50 , 200 , 25 , 40]
total_vendas = sum(vendas)
print(total_vendas)

#tamanho_lista = len(vendas)
#print(tamanho_lista)

#valor_maximo = max(vendas)
#valor_minimo = min(vendas)

#rint(valor_maximo , valor_minimo)

#print(vendas[3])

#print(len(vendas))

lista_produtos =["notebook" , "telefone", "carteira", "televisao", "computador"]

#for i in range(5):

    #desejocliente = input("Digite um produto ")
    #print(desejocliente.lower() in lista_produtos)

#lista_produtos.append("relogio")
#print(lista_produtos)

lista_produtos.remove("notebook")
print(lista_produtos)

precos = [1000 , 500 , 1500 , 2000]
#precos[0] = precos[0] *1.5
#print(precos)

#print(lista_produtos.count("telefone"))

lista_produtos.sort(reverse=True)
print(lista_produtos)

precos.sort(reverse=True)
print(precos)

vendas.sort(reverse=True)
print(vendas)
