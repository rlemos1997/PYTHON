import os
import PyPDF2 as pp2

merger = pp2.PdfMerger()    

listapdf = os.listdir("pdftreino")

for arquivos in listapdf:
    merger.append(f"pdftreino/{arquivos}")

merger.write("arquivo_combinado.pdf")







