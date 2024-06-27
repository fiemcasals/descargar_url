from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, AudioFileClip

try:
    print("Inicio del script")

    # URL del video de YouTube que deseas descargar
    video_url = 'https://www.youtube.com/watch?v=z6dw-KBjpaM&list=PLb2yscCiJP4ELYxonQivjoDag1SBifFZ9&index=8'
    print(f"URL del video: {video_url}")

    # Carpeta de descargas en tu computadora
    downloads_folder = '/home/mauri/Vídeos'
    print(f"Carpeta de descargas: {downloads_folder}")

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
    print(f'Ocurrió un error: {e}')
