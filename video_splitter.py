from moviepy.editor import VideoFileClip
import os
from tkinter import filedialog
import tkinter as tk

def seleccionar_video():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Seleccionar video")
    return file_path

def obtener_duración_clips():
    clip_duration = int(input("Ingrese la duración de los clips en segundos: "))
    return clip_duration

def obtener_output_dir():
    root = tk.Tk()
    root.withdraw()
    output_dir = filedialog.askdirectory(title="Seleccionar carpeta de destino")
    return output_dir

def recortar_pelicula(video_path, output_dir, clip_duration):
    video = VideoFileClip(video_path)
    total_clips = int(video.duration / clip_duration)
    remaining_duration = video.duration % clip_duration
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i in range(total_clips):
        start_time = i * clip_duration
        end_time = (i + 1) * clip_duration
        clip = video.subclip(start_time, end_time)
        clip_path = os.path.join(output_dir, f"clip_{i+1}.mp4")
        clip.write_videofile(clip_path)
    
    if remaining_duration > 0:
        start_time = total_clips * clip_duration
        end_time = total_clips * clip_duration + remaining_duration
        last_clip = video.subclip(start_time, end_time)
        last_clip_path = os.path.join(output_dir, f"clip_{total_clips + 1}.mp4")
        last_clip.write_videofile(last_clip_path)
    video.close()

if __name__ == "__main__":
    video_path = seleccionar_video()
    if video_path:
        clip_duration = obtener_duración_clips()
        output_dir = obtener_output_dir()
        recortar_pelicula(video_path, output_dir, clip_duration)
    else:
        print("No se seleccionó ningún video.")
