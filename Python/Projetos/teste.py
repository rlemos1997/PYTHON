from pytube import YouTube

# Teste com uma URL de vídeo do YouTube
video_url = 'https://www.youtube.com/watch?v=7NK_JOkuSVY'
yt = YouTube(video_url)
print(yt.title)