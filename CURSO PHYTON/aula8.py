import os
#import datetime
#print(datetime.date.today())
#print(os.listdir("arquivos"))
lista_arquivos = os.listdir("arquivos")
#print(lista_arquivos)

#for arquivo in lista_arquivos:
    #if ".txt" in arquivo:
        #if "22" in arquivo:
            #os.rename("arquivos/abr22.txt" , "arquivos/22/abr22.txt")
for arquivo in lista_arquivos:
    if ".txt" in arquivo:
        if "22" in arquivo:
            os.rename(f"arquivoS/{arquivo}" , f"arquivoS/22/{arquivo}")
        else:
            os.rename(f"arquivoS/{arquivo}" , f"arquivoS/23/{arquivo}")

print("SOU BRABO")