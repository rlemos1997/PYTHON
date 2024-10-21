from random import randint
import time 

def linhas():
    print('-' * 30)


def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)



titulo('JOGO DA ADIVINHACAO')
titulo ('VAMOS JOGAR')
titulo('JOGO DA FORCA')

def nomes(*nome):
    print("-" * 30)
    print(nome)
    print("-" * 30)


nomes("Ricardo" , "lemos" , "Victória")
nomes('Renato' , 'Bob')
nomes('Yumi' , 'Lira')