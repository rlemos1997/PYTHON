salario_vendedor= 2000
vendas = 2500
vendas_empresa = 25000
meta_empresa = 30000
meta1 = 1000
meta2 = 1500
meta3 = 2000

if vendas > meta3:
    if vendas_empresa < meta_empresa:
        
        print("A empresa não bateu a meta")
    print("O Vendedor bateu a meta 3")
    bonus = vendas * 0.2
    print("O valor do bonus é: " , bonus)
    salario_vendedor= salario_vendedor + bonus
    print("Seu salario com o bonus é:" , salario_vendedor)

elif vendas > meta2:
    if vendas_empresa < meta_empresa:
        print("A empresa não bateu a meta")
    print("O vendedor bateu a meta 2, parabéns!")
    bonus = vendas * 0.15
    print(" O valor do bonus é de:" , bonus)
    salario_vendedor = salario_vendedor + bonus
    print("Seu salario é de: R$",salario_vendedor)

elif vendas > meta1:
    if vendas_empresa < meta_empresa:
        print("A empresa não bateu a meta")
    print("O Vendedor bateu a meta 1, Parabéns")
    bonus = vendas * 0.1
    print("O valor do bonus é de R$", bonus)
    salario_vendedor = salario_vendedor + bonus
    print("O seu salario é de R$",salario_vendedor)
else:
    print("O vendedor não atingiu a meta")
    print("Seu salario é de:" , salario_vendedor)

lista_produtos = ["telefone" , "computador" , "notebook" , "televisão"]
produto_desejado = input("Digite o produto desejado ")
produto_desejado.lower()

if produto_desejado in lista_produtos:
    print("Produto em estoque")
else:
    print("Infelizmente não temos esse produto")

print("Hello world!")