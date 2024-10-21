# 1 PASSO IMPORTANDO BIBLIOTECAS QUE VAMOS UTILIZAR

from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import tkinter as tk
from tkinter import filedialog

# 2 PASSO BAIXANDO OS VIDEOS E CONVERTENDO EM MP3

def baixar_video_para_mp3(url, destino):
    try:
        video = YouTube(url) #PEGANDO O VIDEO DA URL FORNECIDA PELO USUARIO
        stream = video.streams.filter(only_audio=True).first() #FILTRANDO APENAS O AUDIO DO VIDEO
        arquivo_baixado = stream.download(output_path=destino) #FAZ O DOWNLOAD DO ARQUIVO PAR A PASTA ESCOLHIDA


        base, ext = os.path.splitext(arquivo_baixado)
        arquivoo_mp3 = base + ".mp3"
        video_clip = VideoFileClip(arquivo_baixado) #ABRINDO O ARQUIVO DE VIDEO COM O MOVIEPY
        video_clip.audio.write_audiofile(arquivoo_mp3) #EXTRAINDO O AUDIO E SALVANDO COMO MP3
        video_clip.close()

        os.remove(arquivo_baixado) #REMOVENDO O ARQUIVO ORIGINAL PARA NÃO OCUPAR ESPAÇO

        print(f"Download e conversão de {video.title} concluido!")

    except Exception as e:
        print(f"Erro ao baixar o video: ,{e}")


def escolher_pasta():
    pasta_selecionada = filedialog.askdirectory() # ABRE UMA JANELA PARA O USUARIO ESCOLHER ONDE QUER SALVAR O ARQUIVO
    return pasta_selecionada


def baixar_com_interface(): # QUANDO CLICAR NO BOTAO BAIXAR MP3 A FUNÇÃO BAIXA O VIDEO, CONVERTE PARA MP3 E SALVA NA PASTA ESCOLHIDA
    url = entrada_url.get() #PEGA A URL DIGITADA PELO USUARIO
    destino = escolher_pasta()
    baixar_video_para_mp3(url, destino)


#CRIANDO A JANELA DA INTERFACE
janela = tk.Tk()
janela.title("Youtube para MP3")

#CRIANDO OS CAMPOS DE ENTRADA
rotulo = tk.Label(janela, text="Insira a URL do video:")
rotulo.pack()

entrada_url = tk.Entry(janela, width=50)
entrada_url.pack()

botao_baixar = tk.Button(janela, text="Baixar Mp3", command=baixar_com_interface)
botao_baixar.pack()


janela.mainloop()



def baixar_playlist_para_mp3(url, destino):
    try:
        playlist = Playlist(url) #PEGA A URL DA PLAYLIST FORNECIDA
        print(f"Baixando playlist: {playlist.title}")

        for video in playlist.videos: # VAI PASSANDO POR TODOS OS VIDEOS DA PLAYLIST
            baixar_video_para_mp3(video.watch_url, destino) #BAIXA UM VIDEO POR VEZ USANDO A FUNÇÃO BAIXAR VIDEO PARA MP3
        print(f"Download da Playlist {playlist.title} concluido!")

    except Exception as e:
        print(f"Ocorreu um erro ai baixar a plylist:, {e}")
        