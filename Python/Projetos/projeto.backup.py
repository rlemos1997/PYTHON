import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

caminho_pasta_selecionada = askdirectory()

data_atual= datetime.datetime.today().strftime("%d-%m-%Y %H%M%S")

lista_arquivos = os.listdir(caminho_pasta_selecionada)

nome_pasta_backup2 = f"backup2"
caminho_pasta_backup = f"{caminho_pasta_selecionada}/{nome_pasta_backup2}"
if not os.path.exists(caminho_pasta_backup):
    os.mkdir(caminho_pasta_backup)


for arquivo in lista_arquivos:
    caminho_arquivo = f"{caminho_pasta_selecionada}/{arquivo}"
    caminho_final_arquivo = f"{caminho_pasta_backup}/{data_atual}/{arquivo}"
    if "." in arquivo:
        shutil.copy2(caminho_arquivo , caminho_final_arquivo)
    elif "backup2" != arquivo:
        shutil.copytree(caminho_arquivo , caminho_final_arquivo)