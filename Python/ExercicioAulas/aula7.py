
dic_produtos = {"telefone":2000 , "computador":5000, "televisão":3000 , "video game":1500}
#print(dic_produtos["video game"])

#dic_produtos["telefone"] = dic_produtos["telefone"] * 1.1
#print(dic_produtos)

#quantidade_produtos = len(dic_produtos)
#print(quantidade_produtos)

#dic_produtos.pop("telefone")
#print(dic_produtos)

#ic_produtos["caixa de som"] = 1000
#dic_produtos["relógio"] = 500
#dic_produtos["cafeteira"] = 655
#print(dic_produtos)

#dic_produtos.pop("caixa de som")
#dic_produtos.pop("relógio")
#dic_produtos.pop("cafeteira")
#print(dic_produtos)

#if "telefone" in dic_produtos:
    #print("Temos em estoque")
#else:
    #print("não temos esse produto no estoque")

#if 3000 in dic_produtos.values():
    #print("temos um produto desse valor no estoque")
#else:
    #print("não temos um produto nesse valor")

#print(dic_produtos.values())


#nome_produto = input("Digite o nome do produto ")
#valor_produto = input("Digite o valor do produto ")

#nome_produto = nome_produto.lower()
#valor_produto = int(valor_produto)

#dic_produtos[nome_produto] = valor_produto
#print(dic_produtos)

for produto in dic_produtos:
    dic_produtos[produto] = dic_produtos[produto] * 1.1

print(dic_produtos)