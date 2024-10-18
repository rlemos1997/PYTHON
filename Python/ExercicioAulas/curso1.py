import os
import pandas as pd
import plotly.express as px
from tkinter.filedialog import askdirectory

pasta_arquivos = askdirectory()

arquivos_vendas = os.listdir(pasta_arquivos)
for arquivo in arquivos_vendas:
    lista_arquivos = (f"{pasta_arquivos}/{arquivo}")
    tabela = pd.read_csv(lista_arquivos)
    if "vendas" in arquivo.lower():
        print(f"{pasta_arquivos}/{arquivo}")
        
tabela_total = pd.DataFrame()

for arquivo in arquivos_vendas:
    if "vendas" in arquivo.lower():
        print(f"{pasta_arquivos}/{arquivo}")
        tabela_total = pd.concat([tabela_total, tabela])
      
tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida" , ascending=False)
print(tabela_produtos)

tabela_total["Faturamento"] = tabela_total["Quantidade Vendida"] * tabela_total["Preco Unitario"]

tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento" , ascending=False)
print(tabela_faturamento)

tabela_loja_faturamento = tabela_total.groupby("Loja").sum()
tabela_loja_faturamento = tabela_loja_faturamento[["Faturamento"]]
print(tabela_loja_faturamento)

grafico = px.bar(tabela_loja_faturamento, x=tabela_loja_faturamento.index, y="Faturamento")
grafico.show()