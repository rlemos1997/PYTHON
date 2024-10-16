# ENTRAR NO SISTEMA DA EMPRESA
import pyautogui
import time
import pandas as pd
import os

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("brave")
pyautogui.press("enter")

time.sleep(3)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=529, y=370)
pyautogui.write("rlemos@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123456")
pyautogui.click(x=663, y=520)

time.sleep(2)

lista_produtos = pd.read_csv
print(lista_produtos)

tabela= pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    codigo = tabela.loc[linha , "codigo"]
    pyautogui.click(x=451, y=252)
    pyautogui.write(str(codigo))
    
    marca = tabela.loc[linha , "marca"]
    pyautogui.press("tab")
    pyautogui.write(str(marca))

    tipo = tabela.loc[linha , "tipo"]
    pyautogui.press("tab")
    pyautogui.write(str(tipo))

    categoria = tabela.loc[linha , "categoria"]
    pyautogui.press("tab")
    pyautogui.write(str(categoria))

    preco = tabela.loc[linha , "preco_unitario"]
    pyautogui.press("tab")
    pyautogui.write(str(preco))

    custo = tabela.loc[linha , "custo"]
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    
    observacao = tabela.loc[linha , "obs"]
    pyautogui.press("tab")
    pyautogui.write(str(observacao))


    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
