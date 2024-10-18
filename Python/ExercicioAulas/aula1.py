faturamento = 800
custo = 300
novas_vendas = 100
faturamento = faturamento + novas_vendas

imposto = faturamento * 0.1
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("o lucro foi de:" , lucro)
print("a margem de lucro foi de:" , round(margem_lucro , 2))

meses_contrato = 210
contrato_anos = 170/12
print("O tempo total de contrato é de:" , int(contrato_anos) , "anos e" , meses_contrato % 12 , "meses")
