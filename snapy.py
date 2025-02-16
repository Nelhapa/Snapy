from tkinter import * #Biblioteca de interface.
from yt_dlp import YoutubeDL #Biblioteca para baixar áudio de vídeos do YouTube.
from plyer import notification #Biblioteca para notificação.

def obter_texto(): #Função para o áudio do vídeo a partir da URL fornecida.
    url = entrada.get() #Pega o que foi digitado.
    if not url.strip(): #Verifica se o campo não está vazio.
        return

    ydl_opts = {  # Configurações para o download do áudio.
    'format': 'bestaudio/best',
    'outtmpl': '/.../.../.../%(title)s.%(ext)s',  #Caminho aonde tu deseja deixar os áudios.
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
  
    
    with YoutubeDL(ydl_opts) as ydl:  #Inicia o download do áudio.
     ydl.download([url])
    entrada.delete(0, END) #Limpa o campo de entrada após o download.

    notification.notify( #Notificação quando o download foi concluído.
    message='Download concluído.',
    timeout=10,
)

#Interface gráfica.
janela = Tk()
janela.title("Snapy")
texto_url = Label(janela, text="Insira a URL da música que deseja baixar:")
texto_url.pack()
entrada = Entry(janela) 
entrada.pack()
bota_download = Button(janela, text="Baixar", command=obter_texto)
bota_download.pack()

janela.mainloop()