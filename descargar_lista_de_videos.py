from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, AudioFileClip

def descargar_video(video_url, downloads_folder):
    try:
        print(f"Inicio del proceso para: {video_url}")

        # Crear el objeto YouTube
        yt = YouTube(video_url)
        print("Objeto YouTube creado")

        # Seleccionar el stream de video de mayor resolución
        video_stream = yt.streams.filter(only_video=True, file_extension='mp4').order_by('resolution').desc().first()
        # Seleccionar el stream de audio
        audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').order_by('abr').desc().first()

        if not video_stream or not audio_stream:
            raise Exception("No se encontraron streams de video o audio adecuados")

        # Descargar los streams de video y audio
        print(f'Descargando video: {yt.title}...')
        video_path = video_stream.download(output_path=downloads_folder, filename='video.mp4')
        audio_path = audio_stream.download(output_path=downloads_folder, filename='audio.mp4')
        print('Descargas completas')

        # Combinar video y audio usando moviepy
        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.set_audio(audio_clip)
        final_output_path = os.path.join(downloads_folder, yt.title + '.mp4')
        final_clip.write_videofile(final_output_path, codec='libx264', audio_codec='aac')

        # Borrar los archivos temporales de video y audio
        os.remove(video_path)
        os.remove(audio_path)

        print(f'Video final descargado en {final_output_path}')
    except Exception as e:
        print(f'Ocurrió un error con el video {video_url}: {e}')

# Lista de URLs de videos de YouTube que deseas descargar
video_urls = [

    'https://www.youtube.com/watch?v=odmC2m_aKak&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=1&pp=iAQB',
    'https://www.youtube.com/watch?v=AipqUgfeZTA&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=2&pp=iAQB',
    'https://www.youtube.com/watch?v=0Oy5y-ecodA&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=3&pp=iAQB',
    'https://www.youtube.com/watch?v=ENLUevRVPz8&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=4&pp=iAQB',
    'https://www.youtube.com/watch?v=I4m0nsug6i8&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=5&pp=iAQB',
    'https://www.youtube.com/watch?v=THqQCoPJtB0&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=6&pp=iAQB',
    'https://www.youtube.com/watch?v=3PycQQrm33g&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=7&pp=iAQB',
    'https://www.youtube.com/watch?v=z6dw-KBjpaM&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=8&pp=iAQB',
    'https://www.youtube.com/watch?v=kS03fr-uAx8&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=9&pp=iAQB',
    'https://www.youtube.com/watch?v=8i0BKF6qiQo&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=10&pp=iAQB',
    'https://www.youtube.com/watch?v=wPoD0Pecu_4&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=11&pp=iAQB',
    'https://www.youtube.com/watch?v=sGlkYoc_IY8&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=12&pp=iAQB',
    'https://www.youtube.com/watch?v=Nj0i-Ao7jAw&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=13&pp=iAQB',
    'https://www.youtube.com/watch?v=73ohc0JR0zk&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=14&pp=iAQB',
    'https://www.youtube.com/watch?v=OwnYnk-HoM8&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=15&pp=iAQB',
    'https://www.youtube.com/watch?v=EXQkVBuPdaM&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=16&pp=iAQB',
    'https://www.youtube.com/watch?v=opUplhP5psg&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=17&t=4253s&pp=iAQB',
    'https://www.youtube.com/watch?v=X2WLFYw8DLM&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=18&pp=iAQB',
    'https://www.youtube.com/watch?v=k1chI2uo6qA&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=19&pp=iAQB',
    'https://www.youtube.com/watch?v=e3yxa8aEDnc&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=20&pp=iAQB',
    'https://www.youtube.com/watch?v=hs44KMxY4XE&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=21&t=1708s&pp=iAQB',
    'https://www.youtube.com/watch?v=j7wB811AE6s&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=22&t=1021s&pp=iAQB',
    'https://www.youtube.com/watch?v=TVtw8QtnHRE&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=23&t=3676s&pp=iAQB',
    'https://www.youtube.com/watch?v=3PqildmehPM&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=24&pp=iAQB',
    'https://www.youtube.com/watch?v=05NHkTucOSQ&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=25&pp=iAQB',
    'https://www.youtube.com/watch?v=RdUnwJ2iWzY&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=26&pp=iAQB',
    'https://www.youtube.com/watch?v=aqDaaLjgDL4&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=27&pp=iAQB',
    'https://www.youtube.com/watch?v=QybluAXEvJw&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=28&t=677s&pp=iAQB',
    'https://www.youtube.com/watch?v=HAEpwzWdrMg&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=29&t=722s&pp=iAQB',
    'https://www.youtube.com/watch?v=N2TqZBIfZOc&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=30&pp=iAQB',
    'https://www.youtube.com/watch?v=G4hU1mi5avE&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=31&pp=iAQB',
    'https://www.youtube.com/watch?v=N5d3pE9RZTA&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=32&pp=iAQB',
    'https://www.youtube.com/watch?v=WxDlkopSiQI&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=33&pp=iAQB',
    'https://www.youtube.com/watch?v=QOohhjM3p1E&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=34&pp=iAQB',
    'https://www.youtube.com/watch?v=5xRkdylyhpA&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=35&pp=iAQB',
    # Agrega más URLs aquí
]

# Carpeta de descargas en tu computadora
downloads_folder = '/home/mauri/Vídeos'
print(f"Carpeta de descargas: {downloads_folder}")

# Descargar cada video de la lista
for url in video_urls:
    descargar_video(url, downloads_folder)

